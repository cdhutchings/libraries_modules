from os_handling_modules import *

# Takes any functions defined in the "from" part of the import, and imports them all (*)
secret_encoded_file = encode("standard_library.py")
print(secret_encoded_file)

decoded_file = decode(secret_encoded_file)
print(decoded_file)