import argon2

def encryptor(password):
    '''hashing portion aka encryption'''
    #code adapted from https://cryptobook.nakov.com/mac-and-key-derivation/argon2
    
    #master_password = input("Please enter your master password: ")
    argon2Hasher = argon2.PasswordHasher(
        time_cost=16, 
        memory_cost=2**15, 
        parallelism=2, 
        hash_len=32, 
        salt_len=16)

    hash = argon2Hasher.hash(password)
    return hash

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


