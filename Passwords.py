#Author         : Chua Philip
#Name of program: CIPM - Cybersecurity Integrated Password Manager
#Program name   : Passwords.py
#Description    : This holds the functions that utilize the entered password and generated salt file as well as to setup the file encryptor and decryptor.
#First written on: 19/02/2023
#Last modified  : 19/03/2023

import argon2
import base64
import secrets
import random
import string
import hashlib
import requests

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

'''------------------------------------------------------------------------
function to check if the stored passwords has been compromised
---------------------------------------------------------------------------'''
def checkPwnedPasswords(password):
    sha_password = hashlib.sha1(password.encode()).hexdigest() #hashes the password for comparison with the API request
    sha_prefix = sha_password[0:5] #takes the first 5 characters of the hash
    sha_postfix = sha_password[5:].upper() #takes the remaining characters of the hash
    
    #API requests that returns a list of compromised hashs starting with the first 5 hashed characters
    url = 'https://api.pwnedpasswords.com/range/' + sha_prefix

    pwnedDict = {} #dictionary to store the hash and number of occurences

    response = requests.request("GET", url, headers={}, data={})
    pwnList = response.text.split('\r\n') #split by newline/return (enter key)
    for pwnedPass in pwnList:
        pwnedHash = pwnedPass.split(':') 
        pwnedDict[pwnedHash[0]] = pwnedHash[1] #stores the hash : number of occurences in a dictionary
    
    if sha_postfix in pwnedDict.keys(): #checks if the hash is in the dictionary
        dictToReturn = {password:pwnedDict[sha_postfix]} #creates a new dictionary with the hash and number of occurences
        return dictToReturn
    else:
        return False