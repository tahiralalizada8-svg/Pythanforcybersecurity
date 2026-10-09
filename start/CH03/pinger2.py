#!/usr/bin/env python3
# First example of pinging from Python
# By 

import os

# Assign prefix
ip-prefix = "192.168.0."

# start loop
for final octet in range(10):
    # set ip adress
    # adress = ip-prefx + final-octet

    # Build ping CMD
    # ping_cmd = f"ping -c 1 -w 1 {address} > /dev/null 2>&]"

# Run ping 
status_code = os.system( ping_cmd )

#print status
#print(status_code)
if status_code == 0:
    print("ONLINE")
else:
    print("offline")