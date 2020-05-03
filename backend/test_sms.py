"""
    Test the sms module
"""

import unittest
from sms import API

class SMSTester(unittest.TestCase):

    def setUp(self) -> None:
        self.api = API("India")
        self.api.getAll()

    def test_API(self):
        self.assertTrue(len(self.api.buildMessage()) > 0 )




if __name__ == "__main__":
    unittest.main()