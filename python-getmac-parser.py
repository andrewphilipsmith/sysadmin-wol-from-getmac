import os.path
import re

regx_pattern = r"""
 ^local area connection.*?,              # one of the connector named LAN
 (?!vmware virtual).*?,                  # not one of the VMware devices
 (?P<mac>([0-9A-F]{2}-){5}([0-9A-F]{2})) # get the MAC address itself
 ,.*?$                                   # look to the end of the line
 """
regx_pattern = r"^.?local area connection,(?!vmware virtual).*?,(?P<mac>([0-9A-F]{2}-){5}([0-9A-F]{2})),.*?$"

regx_pattern = r'^"?local area connection.*?"?,(?!"?vmware virtual).*?,"?(?P<mac>([0-9A-F]{2}-){5}([0-9A-F]{2}))"?,.*?$'

# Regex pattern
pattern = re.compile(regx_pattern, re.IGNORECASE | re.MULTILINE)


for laptop_number in range(10,100):

    getmac_dir = r"Y:\logs\wpkg\getmac"
    getmac_file_name = os.path.join(getmac_dir, "getmac-MA-LAPTOP{}.csv".format(laptop_number))
    # print getmac_file_name
    if os.path.exists(getmac_file_name):
        f = open(getmac_file_name, 'r')
        text = f.read()
        # print text
        for match in pattern.finditer(text):
            mac_long_form = match.group('mac')
            mac = re.sub(r"-", "", mac_long_form)
            print laptop_number, mac_long_form, mac
        f.close()
    #else:
        # print "file not found"