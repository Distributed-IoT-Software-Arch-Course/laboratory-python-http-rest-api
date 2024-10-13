from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.device_resource import DeviceResource
from resources.devices_resource import DevicesResource
from persistence.data_manager import DataManager
from model.device_model import DeviceModel

# Create Flask App
app = Flask(__name__)

# Create RESTful API
api = Api(app)

# Define API Endpoint Prefix
ENDPOINT_PREFIX = "/api/iot/inventory"

print("Starting HTTP RESTful API Server ...")

# Create Data Manager to handle the data of devices
data_manager = DataManager()

# Create a demo device for the API and its testing
demoDevice = DeviceModel("device00001", "iot:demosensor", "v0.0.0.1", "Acme-Inc")

# Add the demo device to the data manager
data_manager.add_device(demoDevice)

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

# Start the Flask App
if __name__ == '__main__':

    # Start the Flask App on port 7070
    app.run(host='0.0.0.0', port=7070)
