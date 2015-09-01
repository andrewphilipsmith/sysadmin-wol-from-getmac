import argparse
import os.path
import re


_pattern = None


def _set_regex():
    if _pattern is not None:
        return _pattern
    else:
        regx_pattern = r'^"?local area connection.*?"?,' \
                       r'(?!"?vmware virtual).*?,' \
                       r'"?(?P<mac>([0-9A-F]{2}-){5}([0-9A-F]{2}))"?,.*?$'

        # Regex pattern
        return re.compile(regx_pattern, re.IGNORECASE | re.MULTILINE)


def wired_mac_from_getmac(getmac_text):
    pattern = _set_regex()
    result = ()
    for match in pattern.finditer(getmac_text):
        mac_long_form = match.group('mac')
        result += (mac_long_form,)

    return result


for laptop_number in range(10,100):

    getmac_dir = r"Y:\logs\wpkg\getmac"
    getmac_file_name = os.path.join(getmac_dir, "getmac-MA-LAPTOP{}.csv".format(laptop_number))
    # print getmac_file_name
    if os.path.exists(getmac_file_name):
        f = open(getmac_file_name, 'r')
        text = f.read()
        # print text
        wired_mac_from_getmac(text)
        f.close()
    #else:
        # print "file not found"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="wol4getmac sends Wake On LAN (WOL) signals to clients whose network interface details have been"
                    "captured using the Windows 'getmac' command. Gets the output from the 'getmac' command as the argument,"
                    "rather than requiring the MAC address itself. A WOL command should be sent of all of the target's"
                    "devices with the string 'Local Area Connection' in their name, which are not 'VMWare Virtual' "
                    "device types. In most cases this only a single device which fits this requirement."
    )
    # positional, rather than option.
    parser.add_argument(
        '-d', '--directory', help="The directory containing the 'getmac' output files."
    )
    parser.add_argument(
        '-f', '--filename-regex',
        help="(Optional) A regular expression (regex) to match filenames in the directory. Only those files which match "
             "the regex will be processed.")
    args = parser.parse_args()
    main(args)
