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
        self.device.connect_to_car(True)

    def disconnect_to_device(self):
        self.device.connect_to_car(False)

    def get_actual_speed(self):
        self.speed = self.device.measure_speed()['speed']

    def get_actual_gas_level(self):
        self.gas = self.device.measure_gas()['gas']
