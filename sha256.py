import hashlib
import os
import datetime                                         
def sha256(text):
    hash_input = inout("Hash: ")
    decripty = hashlib.sha256(text.decode().hexdigest())
    return descripty



if __name__ == "__main__":
    sha256()
