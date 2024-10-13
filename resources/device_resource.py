from json import JSONDecodeError
from flask import request, Response
from flask_restful import Resource
from model.device_model import DeviceModel

class DeviceResource(Resource):
    """ Device Resource Class extends Resource from Flask-RESTful to implement the HTTP Methods and RESTful API """

    def __init__(self, **kwargs):
        """ Constructor """

        # Read the data manager from the keyword arguments and store it in the instance variable
        self.dataManager = kwargs['data_manager']

    def get(self, device_id):
        """ Handle HTTP GET Request for the Device Resource """

        # Check if the device exists in the data manager
        if device_id in self.dataManager.device_dictionary:
            # Return the device data as JSON with HTTP status code 200
            return self.dataManager.device_dictionary[device_id].__dict__, 200
        else:
            return {'error': "Device Not Found !"}, 404

    def put(self, device_id):
        """ Handle HTTP PUT Request for the Device Resource """
        try:
            # Check if the device exists in the data manager
            if device_id in self.dataManager.device_dictionary:
                # The boolean flag force the parsing of POST data as JSON irrespective of the mimetype
                json_data = request.get_json(force=True)

                # Create a new DeviceModel object from the JSON data
                device_model = DeviceModel(**json_data)

                # Check if the UUID in the body matches the UUID in the URL
                if device_model.uuid != device_id:
                    return {'error': "UUID mismatch between body and resource"}, 400
                else:
                    # Update the device in the data manager
                    self.dataManager.update_device(device_model)

                    # Return HTTP status code 204 (No Content)
                    return Response(status=204)
            else:
                return {'error': "Device UUID not found"}, 404
        except JSONDecodeError:
            return {'error': "Invalid JSON ! Check the request"}, 400
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500

    def delete(self, device_id):
        """ Handle HTTP DELETE Request for the Device Resource """
        try:
            # Check if the device exists in the data manager
            if device_id in self.dataManager.device_dictionary:

                # Remove the device from the data manager
                self.dataManager.remove_device(device_id)

                # Return HTTP status code 204 (No Content)
                return Response(status=204)
            else:
                return {'error': "Device UUID not found"}, 404
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500