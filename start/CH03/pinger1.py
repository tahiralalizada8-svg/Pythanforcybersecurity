#!/usr/bin/env python3
# First example of pinging from Python
# By 

import os

#set Ip address
address = "192.168.0.250"

# Build ping CMD
ping_cmd = f"ping -c 1 -w 1 {address} > /dev/null 2>&]"

# Run ping 
status_code = os.system( ping_cmd )

#print status
#print(status_code)
if status_code == 0:
    print("ONLINE")
else:
    print("offline")

    