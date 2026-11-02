#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By tahira 10/26

# imports
import sys

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
    # f = open(file_path, "w")
    f = open (file_path,"r")

    #read contents
    contents = f.readlines()
    return contents 

    # close
    f.close()
# create hash function
def create_hash(password, salt):
    hashed_pass = sha512_crypt.using(rounds=5000).hash(
        password, 
        salt=salt
        )
    return hashed_pass

# Get input from user
sample_hash = "test:$6$O9OcwTwNbVKqK24q$FuVUpZsHC5uLLBSxUKYYpu6NzuSo/6tkmAyet8XyUsDy9g8v7WkEXbl4Rj6MW45xjl9Hyn15OGUdOPdkfJvVS.:18886:0:99999:7:::"
shadow_line = input("Line from shadow file: ") or sample_hash

# seprate picesess
shadow_parts = shadow_line.split(":")
user_name = shadow_parts[0]
user_hash = shadow_parts[1]
user_salt = user_hash.split("$")[2]

# Load dictionary
password_guesses = load_dictionary("top10000000.txt")
# for each line/guess
for password_guess in password_guesses:
    # Hash guess
    hashed_guess = create_hash(password_guess.strip(), user_salt) 
    # compare hash to guess
    if user_hash == hashed_guess:
        #print guess
        print(user_name, password_guess.strip())
        # quit
        sys.exit()

# print not found
print("Not found")