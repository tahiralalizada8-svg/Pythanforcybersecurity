#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By tahira 10/26

# imports
from passlib.hash import sha512_crypt
import os

# Load dictionary function
def load_dictionary(file_name):
    #Get current directory
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname( script_path )

    #Build file path
    file_path = os.path.join(script_dir, file_name)

    #open file for writing
    f = open(file_path, "r")

    #read contents
    contents = f.read()
    return contents 

# create hash function
def create_hash(password, salt):
    hashed_pass = sha512_crypt.using(rounds=5000).hash(
        password, 
        salt=salt
        )
    return hashed_pass

# Get input from user
# separate picee
# Load dictionary
# for each line/guess
    # Hash guess
    # compare hash to guess
        #print guess
        # quit

# print not found