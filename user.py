from device import Device


class User:
    def __init__(self, **kwargs):
        self.mode = kwargs['mode']
        self.car = kwargs['car']
        self.device = Device(mode=self.mode, car=self.car)
