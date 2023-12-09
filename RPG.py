import secrets
import string
import random

def RandPassGen():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    selection_list = letters + digits + special_chars

    password_len = 12

    password = ''
    for i in range(password_len):
        password+= ''.join(secrets.choice(selection_list))

    return password