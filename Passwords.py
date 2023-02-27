import argon2
import base64
import secrets
from cryptography.fernet import Fernet


def encryptor(input_password,input_salt):
    '''
    hashing portion aka encryption

    The developer is aware  that hashing and encryption are different.
    However, a hashed password is used to encrypt the password database.

    Function - returns a file encrypting object
    
    '''
    #code adapted from https://cryptobook.nakov.com/mac-and-key-derivation/argon2
    
    #master_password = input("Please enter your master password: ")
    # argon2Hasher = argon2.PasswordHasher(
    #     time_cost=16, 
    #     memory_cost=2**15, 
    #     parallelism=2, 
    #     hash_len=32, 
    #     salt_len=16)

    #code adapted from https://stackoverflow.com/questions/49465692/is-it-possible-to-encrypt-then-decrypt-data-securely-against-a-password-in-pytho
    password_hash = argon2.hash_password_raw(password=input_password, salt=input_salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    encryptor = Fernet(encoded_hash)
    return encryptor
    

def decryptor(input_password,input_salt):
    '''decryption portion'''
    #master_password = input("Please enter your master password: ")
    password_hash = argon2.hash_password_raw(password=input_password, salt=input_salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    decryptor = Fernet(encoded_hash)
    return decryptor

def salter():
    '''salt generator'''
    #code adapted from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    salt = secrets.randbits(32)
    return salt

