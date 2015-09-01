__author__ = 'andy'

import unittest
import fixtures
import tempfile
import shutil
import parse_getmac


class TestGetMacMethods(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    """
    Test the extraction of the correct MAC address(es) from the text produced by the getmac cmd.
    The mac_from_getmac() method should return the MAC addresses from all devices with "Local Area Connection" in its
    name and does not have a "VMWare Virtual" device type. In most cases this only a single device will fulfil this
    requirement.
    """
    def test_wired_mac_from_getmac(self):
        self.assertEqual(parse_getmac.wired_mac_from_getmac(fixtures.regular_getmac_output),
                         fixtures.regular_correct_mac)
        self.assertEqual(parse_getmac.wired_mac_from_getmac(fixtures.regular_getmac_output_quotes),
                         fixtures.regular_correct_mac)
        self.assertEqual(parse_getmac.wired_mac_from_getmac(fixtures.multiple_devices_getmac_output),
                         fixtures.multiple_devices_correct_mac)

    def test_get_files(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()