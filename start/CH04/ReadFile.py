#!/usr/bin/env python3
# Sample script that reads from a file
# By 


#Import
import os

#Get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname( script_path )

#Build file path
file_path = os.path.join(script_dir, "testfile.txt")

#open file for writing
f = open(file_path, "r")

#read contents
contents = f.read()
print(contents)

#close
f.close()