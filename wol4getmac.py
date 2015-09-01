import argparse
import inspect
import os.path
import re
import sys

cur_dir = os.path.realpath(os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe()))))

wol_dir = os.path.join(cur_dir, 'pywakeonlan', 'wakeonlan')
print wol_dir
if wol_dir not in sys.path:
    sys.path.append(wol_dir)

import wol

_pattern = None


# TODO: I'm sure that this could be handled more elegantly handed using a closure.
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


def get_files(dir_path, file_name_regex):
    # Create regex on filename
    if file_name_regex is None:
        file_name_regex = ""

    rx = re.compile(file_name_regex, re.IGNORECASE)

    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if 0 == len(file_name_regex) or rx.match(file_name):
                file_list.append(os.path.join(root, file_name))

    return file_list


def main(args):
    dir_path = args.directory
    file_name_regex = args.regex

    for getmac_file_name in get_files(dir_path, file_name_regex):
        if os.path.exists(getmac_file_name):
            f = open(getmac_file_name, 'r')
            text = f.read()
            f.close()

            macs = wired_mac_from_getmac(text)
            print "Sending WOL magic pack to {}, extracted from {}". format(macs, getmac_file_name)
            for mac in macs:
                wol.send_magic_packet(mac)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="wol4getmac sends Wake On LAN (WOL) signals to clients whose network interface details have been "
                    "captured using the Windows 'getmac' command. Gets the output from the 'getmac' command as the "
                    "argument, rather than requiring the MAC address itself. A WOL command should be sent of all of "
                    "the target's devices with the string 'Local Area Connection' in their name, which are not "
                    "'VMWare Virtual' device types. In most cases this only a single device which fits this "
                    "requirement."
    )
    parser.add_argument(
        '-d', '--directory', help="The directory containing the 'getmac' output files."
    )
    parser.add_argument(
        '-f', '--regex',
        help='(Optional) A regular expression (regex) to limit the file names in the directory. Only those filesnames '
             'which match the regex will be processed.')
    g_args = parser.parse_args()
    main(g_args)
