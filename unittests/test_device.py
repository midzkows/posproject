"""
Class containing unittests to Device class,
Always includes positive and negative case
There is no convention to add docstring to unittests.

"""

import unittest

from libs.device import Device


class TestDevice(unittest.TestCase):
    device = Device(car="audi", mode="kierowca")

    def test_connect_to_car_true(self):
        self.device.connect_to_car(True)
        self.assertDictEqual(self.device.connected, {"info": "audi-kierowca", "state": True})

    def test_connect_to_car_false(self):
        self.device.connect_to_car(False)
        self.assertDictEqual(self.device.connected, {"info": "audi-kierowca", "state": False})


if __name__ == '__main__':
    unittest.main()