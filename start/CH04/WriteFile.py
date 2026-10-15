#!/usr/bin/env python3
# Sample script that writes to a file
# By me, 10/14

#Import
import os

#Get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname( script_path )

#Build file path
file_path = os.path.join(script_dir, "testfile.txt")

#open file for writing
f = open(file_path, "w")

#write to the file
f.write("Hello World\n")
f.write("my name is Tahira\n")
f.write("I like rubber ducks\n")

#close file
f.close()
