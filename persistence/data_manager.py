from model.device_model import DeviceModel

class DataManager:
    """ Data Manager Class """

    # Initialize the data manager with an empty dictionary to store the devices
    device_dictionary = {}

    def add_device(self, new_device):
        """ Add a new device to the data manager """

        # Check if the new device is a DeviceModel
        if isinstance(new_device, DeviceModel):
            self.device_dictionary[new_device.uuid] = new_device
        else:
            raise TypeError("Error adding new device ! Only DeviceModel are allowed !")

    def update_device(self, updated_device):
        """ Update an existing device in the data manager """

        # Check if the updated device is a DeviceModel
        if isinstance(updated_device, DeviceModel):
            self.device_dictionary[updated_device.uuid] = updated_device
        else:
            raise TypeError("Error updating the device  Only DeviceModel are allowed !")

    def remove_device(self, device_uuid):
        """ Remove a device from the data manager """

        # Check if the device exists in the data manager
        if device_uuid in self.device_dictionary.keys():
            del self.device_dictionary[device_uuid]