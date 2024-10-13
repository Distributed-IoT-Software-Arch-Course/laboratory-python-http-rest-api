from json import JSONDecodeError
from flask import request, Response
from flask_restful import Resource, reqparse
from model.device_model import DeviceModel

class DevicesResource(Resource):
    """ Devices Resource Class extends Resource from Flask-RESTful to implement the HTTP Methods and RESTful API """

    def __init__(self, **kwargs):
        """ Constructor """

        # Read the data manager from the keyword arguments and store it in the instance variable
        self.dataManager = kwargs['data_manager']

    def get(self):
        """ Handle HTTP GET Request for the Devices Resource """

        # Create a list of devices from the device dictionary
        device_list = []

        # Iterate over all devices in the device dictionary
        for device in self.dataManager.device_dictionary.values():
            # Append the device data as a dictionary to the list
            device_list.append(device.__dict__)

        # Return the list of devices as JSON with HTTP status code 200
        return device_list, 200

    def post(self):
        """ Handle HTTP POST Request for the Devices Resource """

        try:
            # Read the JSON data from the request body. The boolean flag force the parsing of POST
            # data as JSON irrespective of the mimetype
            json_data = request.get_json(force=True)

            # Create a new DeviceModel object from the JSON data
            device_model = DeviceModel(**json_data)

            # Check if the device UUID already exists in the device dictionary
            if device_model.uuid in self.dataManager.device_dictionary:
                return {'error': "Device UUID already exists"}, 409
            else:
                # Add the device to the data manager
                self.dataManager.add_device(device_model)

                # Return HTTP status code 201 (Created) with the Location header pointing to the new resource
                return Response(status=201, headers={"Location": request.url + "/" + device_model.uuid})
        except JSONDecodeError:
            return {'error': "Invalid JSON ! Check the request"}, 400
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500
