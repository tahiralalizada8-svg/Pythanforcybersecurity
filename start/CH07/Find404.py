#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By tahira 11/02
import os
# open log file
# Get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname( script_path )

#Build file path
file_path = os.path.join(script_dir, "access.log")

#open file for writing
f = open(file_path, "r")

# read line by line
while True: 
    line = f.readline()
    if not line:
        break
    # search for 404
    if"404" in line:
    # print line
     print(line)

f.close()