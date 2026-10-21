#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By tahira 10/21/2026


#86nd2sb-5XWB1BMXJ8dFmyjiW6jjvYDZEi5QmpagvUU=


from cryptography.fernet import Fernet

def creat_key():
    key = Fernet.generate_key()
    key = key.decode()
    return key
def encrypt(key, plain_text):

    # Encode data to bytes object
    key = key.encode()
    plain_text = plain_text.encode()

    # creat fernet object and encrypt
    f = Fernet(key)
    cipher_text = f.encrypt(plain_text)
    cipher_text = cipher_text.decode()
    return cipher_text
def decrypt(key, cipher_text):
    # Encode data to bytes object
    key = key.encode()
    cipher_text = cipher_text.encode()

    # creat fernet object and encrypt
    f = Fernet(key)
    plain_text = f.encrypt(plain_text)
    plain_text = plain_text.decode()
    return plain_text

# ask user what to do
print("""
      Welcome to the encryption tool 
      This tool encrypts and decrypts data
      This uses Fernet Encryption""")
print ("=" * 80)
action = input("Encryppt, Decrypt, or create key (e/d/c) ")
action = action.lower()
action = action[0]

# if creat key
if action =="c":
        key = creat_key()
        print(key)
# else if encrypt
elif action =="e":
    # get key
    key = input("key: ")
    # get message
    message = input("Message: ")
    cipher_text = encrypt(key, message)
    print(cipher_text)
# else if decrypt
elif action =="d":
    # Get key
    key = input("key: ")
     # Get message
    message = input ("Message: ")
    plain_text = decrypt(key, message)
    print(plain_text)


    # get message = input("Message:")



# key = Fernet.generate_key()
# print(key)

# f = Fernet(key)
# plain_text = b"this is my secret"
# cipher_text = f.encrypt(plain_text)

# print(cipher_text)

# print( f.decrypt(cipher_text) )


