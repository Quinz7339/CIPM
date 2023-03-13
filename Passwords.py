#Author         : Chua Philip
#Name of program: CIPM - Cybersecurity Integrated Password Manager
#Program name   : Passwords.py
#Description    : This holds the functions that utilize the entered password and generated salt file as well as to setup the file encryptor and decryptor.
#First written on: 19/02/2023
#Last modified  : 13/03/2023

import argon2
import base64
import secrets
import random
import string
from cryptography.fernet import Fernet

##############################################################################################
######################  functions that interacts with password fields  #######################
##############################################################################################


'''---------------------------------------------------------------
function to establish the object to encrypt the password database
------------------------------------------------------------------'''   
def encryptor(input_password,input_salt):
    '''
    -------------------------------------------------------------------------
    |   Note:                                                               |
    |   The developer is aware that hashing and encryption are different.   |
    |   However, a hashed password is used to encrypt the password database.|
    -------------------------------------------------------------------------
    '''

    #code adapted from https://stackoverflow.com/questions/49465692/is-it-possible-to-encrypt-then-decrypt-data-securely-against-a-password-in-pytho
    password_hash = argon2.hash_password_raw(password=input_password, salt=input_salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    encryptor = Fernet(encoded_hash)
    return encryptor
    
'''---------------------------------------------------------------
function to establish the object to decrypt the password database
------------------------------------------------------------------''' 
def decryptor(input_password,input_salt):
    '''decryption portion'''
    password_hash = argon2.hash_password_raw(password=input_password, salt=input_salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    decryptor = Fernet(encoded_hash)
    return decryptor

'''------------------------------------------------------------------------
function to generate a randomly generated salt to hash the entered password
---------------------------------------------------------------------------''' 
def salter():
    salt = secrets.randbits(32)
    return salt

'''------------------------------------------------------------------------
function to generate a randomly generated password
---------------------------------------------------------------------------''' 
def gen_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
