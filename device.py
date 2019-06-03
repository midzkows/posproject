import random


class Device:
    connected = {'info': '', 'state': False}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self.car = kwargs['car']
        self.mode = kwargs['mode']

    def connect_to_car(self, state):
        """

        :param state:
        :return:
        """
        self.connected = {'info': '-'.join([self.car, self.mode]), 'state': state}
        print "Connection state: %s" % state

    def measure_speed(self):
        """

        :return:
        """
        if self.connected['state']:
            return {'speed': random.randint(10, 200), 'info': 'speed measured'}
        raise RuntimeError('Failed to measure speed')

    def measure_gas(self):
        """

        :return:
        """
        if self.connected['state']:
            return {'gas': random.randint(10, 200), 'info': 'gas measured'}
        raise RuntimeError('Failed to measure gas level')
