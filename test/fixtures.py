"""
Example output from the getmac command and the correctly identified MAC address
"""
regular_getmac_output = r"""
Connection Name,Network Adapter,Physical Address,Transport Name
Local Area Connection,Intel(R) 82579LM Gigabit Network Connection,D4-BE-D9-23-F0-E5,\Device\Tcpip_{21A55F89-50A7-4BD9-B19C-C29F228F716F}
Local Area Connection 2,VMware Virtual Ethernet Adapter for VMnet1,00-50-56-C0-00-01,\Device\Tcpip_{2A6D1686-D575-41E5-8452-8B4CF00144ED}
Local Area Connection 3,VMware Virtual Ethernet Adapter for VMnet8,00-50-56-C0-00-08,\Device\Tcpip_{8FC37923-8B5A-441E-890D-DAB4D22FF19B}
Wireless Network Connection,Intel(R) Centrino(R) Advanced-N 6205,8C-70-5A-1F-0B-AC,\Device\Tcpip_{172044CB-C250-4C6E-A0FA-17AA94D8E588}
Bluetooth Network Connection,Bluetooth Device (Personal Area Network),C0-18-85-DA-13-63,Media disconnected
"""

regular_correct_mac = (r"""D4-BE-D9-23-F0-E5""",)

regular_getmac_output_quotes = r'''
"Connection Name","Network Adapter","Physical Address","Transport Name"
"Local Area Connection","Realtek PCIe GBE Family Controller","D4-BE-D9-23-F0-E5","\Device\Tcpip_{4FEA90EE-E666-4D96-A5E6-86EFCF077C0A}"
"Wireless Network Connection","Dell Wireless 1397 WLAN Mini-Card","F0-7B-CB-72-A7-C7","Media disconnected"
"Local Area Connection 3","VMware Virtual Ethernet Adapter for VMnet1","00-50-56-C0-00-01","\Device\Tcpip_{F0402804-844E-4138-94A8-2B622204C2AF}"
"Local Area Connection 2","VMware Virtual Ethernet Adapter for VMnet8","00-50-56-C0-00-08","\Device\Tcpip_{1AED1EAF-17C7-4D40-946A-5F849FBB726A}"
'''

multiple_devices_getmac_output = r"""
Connection Name,Network Adapter,Physical Address,Transport Name
Local Area Connection,Intel(R) 82579LM Gigabit Network Connection,D4-BE-D9-23-F0-E5,\Device\Tcpip_{21A55F89-50A7-4BD9-B19C-C29F228F716F}
Local Area Connection 2,VMware Virtual Ethernet Adapter for VMnet1,00-50-56-C0-00-01,\Device\Tcpip_{2A6D1686-D575-41E5-8452-8B4CF00144ED}
Local Area Connection 3,VMware Virtual Ethernet Adapter for VMnet8,00-50-56-C0-00-08,\Device\Tcpip_{8FC37923-8B5A-441E-890D-DAB4D22FF19B}
Local Area Connection 4,Intel(R) 82579LM Gigabit Network Connection,D4-BE-D9-23-F0-E6,\Device\Tcpip_{21A55F89-50A7-4BD9-B19C-C29F228F716F}
Wireless Network Connection,Intel(R) Centrino(R) Advanced-N 6205,8C-70-5A-1F-0B-AC,\Device\Tcpip_{172044CB-C250-4C6E-A0FA-17AA94D8E588}
Bluetooth Network Connection,Bluetooth Device (Personal Area Network),C0-18-85-DA-13-63,Media disconnected
"""

multiple_devices_correct_mac = (r"""D4-BE-D9-23-F0-E5""", r"""D4-BE-D9-23-F0-E6""")
