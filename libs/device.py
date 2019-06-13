"""
The C-Car device class containing API methods
"""
import random


class Device:
    connected = {'info': '', 'state': False}

    def __init__(self, **kwargs):
        """
        Object initialisation
        :param kwargs: a dict of params
        """
        self.car = kwargs['car']
        self.mode = kwargs['mode']

    def connect_to_car(self, state):
        """
        Connect C-Car device to car
        :param state: connect or disconnnect
        :type state: bool
        """
        self.connected = {'info': '-'.join([self.car, self.mode]), 'state': state}
        print "Connection state: %s" % state

    def measure_speed(self):
        """
        Measure actual speed
        :return: dict of speed and info
        """
        if self.connected['state']:
            return {'speed': random.randint(10, 200), 'info': 'speed measured'}
        raise RuntimeError('Failed to measure speed')

    def measure_gas(self):
        """
        Measure actual gas level
        :return: dict of gas level and info
        """
        if self.connected['state']:
            return {'gas': random.randint(10, 200), 'info': 'gas measured'}
        raise RuntimeError('Failed to measure gas level')

    def control_speed(self):
        """
        Inform user about the limit of speed
        :return: int
        """
        pass
