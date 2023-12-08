# Importing required module
import base64
from Enc2 import encrypt,decrypt

password = None
try:
    # Read initially set password of Manager
    password = open(".pwd", "r").read()
except IOError:
    pass

# An encoding similar to Vigenère Cipher is used

# Keyword to be used
pwd = "C$_P₹oj#cT"

# Encoding function for the cipher
def encode(string, key=pwd):
    enc = []
    # for i in range(len(string)):
    #     key_c = key[i % len(key)]
    #     # ord() gives the respective ascii value
    #     enc_c = chr(ord(string[i]) + ord(key_c) % 256)
    #     enc.append(enc_c)
    # return base64.urlsafe_b64encode("".join(enc).encode()).decode()
    return encrypt(string, key)

# Function to Decode
def decode(string, key=pwd):
    # dec = []
    # # utf-8 to avoid character mapping errors
    # string = base64.urlsafe_b64decode(string).decode()
    # for i in range(len(string)):
    #     key_c = key[i % len(key)]
    #     dec_c = chr((256 + ord(string[i]) - ord(key_c)) % 256)
    #     dec.append(dec_c)
    # return "".join(dec)
    return decrypt(string,key)
