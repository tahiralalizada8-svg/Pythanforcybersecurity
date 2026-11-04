 #!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By 

# imports
import os
import re 
# open log file
#Get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname( script_path )

#Build file path
file_path = os.path.join(script_dir, "access.log")

#open file for writing
f = open(file_path, "r")
log_lines = f.readlines()

# setup regexr pattren \s\d\d\d\s
search_pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s"
results_dict = {}

# loop throughneach line
for line in log_lines:
    # search for pattern
    m = re.search(search_pattern, line)
    if m:
        #print( m.group(1) )
        # put into dictionary
        result = m.group(1)
        if result in results_dict.keys():
            results_dict[result] += 1
        else:
            results_dict[result] = 1 


# sort by frequency and print
sorted_keys = sorted(results_dict, key=results_dict.get, reverse=False)
for key in sorted_keys:
    print(key, results_dict[key])