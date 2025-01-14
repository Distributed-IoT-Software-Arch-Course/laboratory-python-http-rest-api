import json

class DeviceModel:
    """ Device Model Class """
    def __init__(self, uuid, type, softwareVersion, manufacturer):
        self.uuid = uuid
        self.softwareVersion = softwareVersion
        self.manufacturer = manufacturer
        self.type = type

    def to_json(self):
        """ Convert the object to a JSON String """
        return json.dumps(self, default=lambda o: o.__dict__)