#!/usr/bin/env python3
# Sample script that writes to a file
# By me, 10/14

#Import
import os

#Get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname( script_path )

#Build file path
file_path = os.path.join(script_dir, "hackme.txt")

#open file for writing
f = open(file_path, "w")

#write to the file
f.write("What is your name?\n")
f.write("What is your favorite color?\n")
f.write("What was your first pets's name?\n")
f.write("What is mother's midden name?\n")
f.write("What elementry school did you attend?\n")

#close file
f.close()