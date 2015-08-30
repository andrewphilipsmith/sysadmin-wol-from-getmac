__author__ = 'andy'

import unittest
import fixtures


class TestGetMacMethods(unittest.TestCase):

    """
    Test the extraction of the correct MAC address(es) from the text produced by the getmac cmd.
    The mac_from_getmac() method should return the MAC addresses from all devices with "Local Area Connection" in its
    name and does not have a "VMWare Virtual" device type. In most cases this only a single device will fulfil this
    requirement.
    """
    def test_mac_from_getmac(self):
        self.assertEqual(mac_from_getmac(fixtures.regular_getmac_output),
                         fixtures.regular_correct_mac)
        self.assertEqual(mac_from_getmac(fixtures.multiple_devices_getmac_output),
                         fixtures.multiple_devices_correct_mac)

if __name__ == '__main__':
    unittest.main()