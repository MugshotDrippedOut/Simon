from generate_keys import generate_keys

import hashlib
import base64
import os


def open_file(file):
    with open(file, "r") as f:
        return f.read()


def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)


def create_file(name):
    if not os.path.exists(name):
        with open(name, "w") as f:
            pass


def encrypt(message, n, e):
    n = int(base64.b64decode(n).decode())
    e = int(base64.b64decode(e).decode())
    encrypted = [str(pow(ord(char), e, n)) for char in message]
    encrypted_message = ' '.join(encrypted)
    return base64.b64encode(encrypted_message.encode()).decode()


def decrypt(encrypted_message, n, d):
    n = int(base64.b64decode(n).decode())
    d = int(base64.b64decode(d).decode())
    encrypted_message = base64.b64decode(encrypted_message.encode()).decode()
    encrypted_message = list(map(int, encrypted_message.split()))
    return ''.join(chr(pow(char, d, n)) for char in encrypted_message)


def hash_function(message):
    return hashlib.sha3_512(message.encode("UTF-8")).hexdigest()


def verify(received_hash, message):
    our_hash = hash_function(message)
    if received_hash == our_hash:
        return True
    return False




if __name__ == "__main__":
    #print(open_file("folder\Private_key\Private_key.txt"))
    #print(hash_message("folder\Message\message.txt", "folder\Private_key\Private_key.txt"))
    #print(hash_message("folder\Message\message.txt", "folder\Public_key\Public_key.txt"))
    n, e, d = generate_keys()
    #print(encrypt("Hello World!", n, e))
    #print(decrypt(encrypt("Hello World!", n, e), n, d))
    message = "Hello World!"
    hashed = hash_function(message)
    print("Hashed: ",hashed)
    encrypted = encrypt(hashed, n, e)
    print("Encrypted:", encrypted)
    decrypted = decrypt(encrypted, n, d)
    print("Decrypted:", decrypted)
    print(verify(decrypted, message))