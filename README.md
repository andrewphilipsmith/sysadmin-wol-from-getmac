wol4getmac
==========
wol4getmac sends Wake On LAN (WOL) signals to clients whose network interface details have been captured using the Windows 'getmac' command. Gets the output from the 'getmac' command as the argument, rather than requiring the MAC address itself. A WOL command should be sent of all of the target's devices with the string 'Local Area Connection' in their name, which are not 'VMWare Virtual' device types. In most desktop and laptop computers there will only be a single device which fits this requirement.

Creating the getmac files
-------------------------
The getmac files are created by running the following command on the target computers.
```
%comspec% /c  getmac /v /fo csv > getmac-%COMPUTERNAME%.csv
```

Building it
-----------
To create the wol4getmac as a standalone exe, run the following command. Python v3.3 is required.
```
python setup.py
```

Running it
----------
```
wol4getmac.exe [-d <path\to\directory\containing\getmac\files>] [-f
<"regex to match file names">]
```
