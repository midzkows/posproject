"""
Class containing unittests to User class,
Always includes positive and negative case.
There is no convention to add docstring to unittests.
"""
import unittest
from libs.user import User


class TestUser(unittest.TestCase):
    device = unittest.Mock()
    user = User(car="audi", state="False", device=device)
