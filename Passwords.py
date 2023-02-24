import argon2
import base64
import secrets
from cryptography.fernet import Fernet


def encryptor(password,salt):
    '''
    hashing portion aka encryption

    The developer is aware  that hashing and encryption are different.
    However, a hashed password is used to encrypt the password database.

    Function - returns a file encrypting object
    
    '''
    #code adapted from https://cryptobook.nakov.com/mac-and-key-derivation/argon2
    
    #master_password = input("Please enter your master password: ")
    argon2Hasher = argon2.PasswordHasher(
        time_cost=16, 
        memory_cost=2**15, 
        parallelism=2, 
        hash_len=32, 
        salt_len=16)

    #https://kerkour.com/rust-file-encryption-chacha20poly1305-argon2
    # argon2Hasher = argon2(
    #     hash_length=32,
    #     lanes = 8,
    #     memory_cost=16 *1024,
    #     time_cost=8
    # )


    #code adapted from https://stackoverflow.com/questions/49465692/is-it-possible-to-encrypt-then-decrypt-data-securely-against-a-password-in-pytho
    password_hash = argon2.argon2_hash(password, salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    encryptor = Fernet(encoded_hash)
    return encryptor
    
    hash = argon2Hasher.hash(password)
    print ("raw hash:", hash)
    print (hash[-32:])
    encoded_hash = base64.urlsafe_b64encode(hash[-32:].encode("utf-8"))
    return encoded_hash

def decryptor(password):
    '''decryption portion'''
    #master_password = input("Please enter your master password: ")
    try:
        argon2Hasher = argon2.PasswordHasher(
        time_cost=16, 
        memory_cost=2**15, 
        parallelism=2, 
        hash_len=32, 
        salt_len=16)

        argon2Hasher.verify(hash, password)
        #print ("Correct password.")
        return True
    except:
        #print("Incorrect password.")
        return False

def salter():
    '''salt generator'''
    #code adapted from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    salt = secrets.randbits(32)
    return salt

