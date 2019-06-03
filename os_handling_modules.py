# Modules

# We have been creating and importing modules
# Modules abstract functionality
# They can be complex or simple and might depend on external libraries

import os

working_dir = os.getcwd()
user = os.getlogin()

def return_login():
    return os.getlogin()

def encode(filename):
    return os.fsencode(filename)

def decode(filename):
    return os.fsdecode(filename)
