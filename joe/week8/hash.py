#!/usr/bin/env ipython

# (3) The "hashlib" module allows you to calculate a number of well-known hash
# functions on bytestrings. Ask the user to enter a string, and then use the
# appropriate functions in the "hashlib" module to get the "hex digest" from
# calculating the MD5 digest on the byte equivalent of the input string.

import hashlib

user_input = input("Enter some text to hash: ")

print(hashlib.md5(user_input.encode()).hexdigest())
