#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By 

# ask for message
source_message = input ("what is the message or encrypt/decrypt? ")
source_message = source_message.lower()
final_message =""

# for each letter
for letter in source_message:
    # convert letter to number
    ascii_num = ord(letter)
    
    #if its a letter, add 13
    if ascii_num >=97:
        ascii_num = ascii_num + 13

    #if past z, wrap around
    if ascii_num > 122:
        ascii_num = ascii_num -26

    # convert number to letter
    new_letter = chr(ascii_num)
    
    # Append letter to newmsg
    final_message = final_message + new_letter

#print newmsg
print(final_message)