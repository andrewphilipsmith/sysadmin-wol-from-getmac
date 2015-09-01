__author__ = 'andy'

import unittest
import fixtures
import os
import tempfile
import shutil
import wol4getmac


class TestGetMacMethods(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        for file_name in fixtures.dummy_file_names_all:
            full_file_name = os.path.join(self.tmpdir, file_name)
            open(full_file_name, 'a').close()

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    """
    Test the extraction of the correct MAC address(es) from the text produced by the getmac cmd.
    The mac_from_getmac() method should return the MAC addresses from all devices with "Local Area Connection" in its
    name and does not have a "VMWare Virtual" device type. In most cases this only a single device will fulfil this
    requirement.
    """
    def test_wired_mac_from_getmac(self):
        self.assertEqual(wol4getmac.wired_mac_from_getmac(fixtures.regular_getmac_output),
                         fixtures.regular_correct_mac)
        self.assertEqual(wol4getmac.wired_mac_from_getmac(fixtures.regular_getmac_output_quotes),
                         fixtures.regular_correct_mac)
        self.assertEqual(wol4getmac.wired_mac_from_getmac(fixtures.multiple_devices_getmac_output),
                         fixtures.multiple_devices_correct_mac)

    def test_get_files(self):
        test_pairs = ((fixtures.dummy_file_names_all, ""),
                      (fixtures.dummy_file_names_odd, fixtures.file_name_regex_odd),
                      (fixtures.dummy_file_names_even, fixtures.file_name_regex_even))
        for pair in test_pairs:
            result = ()
            for full_path in wol4getmac.get_files(self.tmpdir, pair[1]):
                result += (os.path.split(full_path)[1],)

            self.assertEqual(result, pair[0])

if __name__ == '__main__':
    unittest.main()