from flask import Flask
from flask_restful import Api
from iot_inventory.resources.device_resource import DeviceResource
from iot_inventory.resources.devices_resource import DevicesResource
from iot_inventory.persistence.data_manager import DataManager
from iot_inventory.model.device_model import DeviceModel

# Define API Endpoint Prefix
ENDPOINT_PREFIX = "/api/iot/inventory"

# Default Host and Port of the HTTP Server
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 7070


def create_server_app(data_manager=None):
    """
    Create and configure the Flask App with the RESTful API resources (App Factory pattern).
    If no Data Manager is provided, a new empty one is created.
    """

    # Create Data Manager to handle the data of devices
    if data_manager is None:
        data_manager = DataManager()

    # Create Flask App
    app = Flask(__name__)

    # Create RESTful API
    api = Api(app)

    # Add Devices Resource to handle the list of devices
    api.add_resource(DevicesResource, ENDPOINT_PREFIX + '/device',
                     resource_class_kwargs={'data_manager': data_manager},
                     endpoint="devices",
                     methods=['GET', 'POST'])

    # Add Device Resource to handle a specific device by its id
    api.add_resource(DeviceResource, ENDPOINT_PREFIX + '/device/<string:device_id>',
                     resource_class_kwargs={'data_manager': data_manager},
                     endpoint='device',
                     methods=['GET', 'PUT', 'DELETE'])

    return app


def load_demo_data(data_manager):
    """ Create Demo Data for the API in order to have some data to work with """

    # Create a demo device for the API and its testing
    demo_device = DeviceModel("device00001", "iot:demosensor", "v0.0.0.1", "Acme-Inc")

    # Add the demo device to the data manager
    data_manager.add_device(demo_device)


def main():
    """ Create demo data and start the Flask App (entry point of the project) """

    # Create Data Manager and fill it with the demo data
    data_manager = DataManager()
    load_demo_data(data_manager)

    # Create the Flask App using the populated Data Manager
    app = create_server_app(data_manager)

    print("Starting HTTP RESTful API Server ...")

    # Start the Flask App on the default host and port (7070)
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT)


# Start the Flask App
if __name__ == '__main__':
    main()
