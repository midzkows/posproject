"""
User class,
contains user methods and parameters

"""

from device import Device


class User:
    def __init__(self, **kwargs):
        self.mode = kwargs['mode']
        self.car = kwargs['car']
        self.device = Device(mode=self.mode, car=self.car)

    speed = None
    gas = None
    current_position = None

    def connect_to_device(self):
        """
        Connect the user to the device
        :return:
        """
        self.device.connect_to_car(True)

    def disconnect_to_device(self):
        """
        Disconnect user from the device
        :return:
        """
        self.device.connect_to_car(False)

    def get_actual_speed(self):
        """
        Get the value of actual speed
        :return:
        """
        self.speed = self.device.measure_speed()['speed']

    def get_actual_gas_level(self):
        """
        Get the value of actual gas level
        :return:
        """
        self.gas = self.device.measure_gas()['gas']

    def change_state(self):
        """
        Change state from driver to mechanic or otherwise
        :return: string
        """
        pass