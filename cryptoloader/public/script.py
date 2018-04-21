#!/usr/bin/python3.6
import requests
import sys
sys.setrecursionlimit(100000)

def bad_encrypting(x):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")
    return x.translate(table)
    
def good_encrypting(x, level):
    if level == 1:
        return bad_encrypting(x)
    else:
        return bad_encrypting(good_encrypting(x, level - 1))

def bad_ciphering(x, key):
    return x ^ key

def good_ciphering(x, key, level):
    if level == 1:
        return bad_ciphering(x, key)
    else:
        return bad_ciphering(good_ciphering(x, key, level - 1), key)

ciphertext = b'\r\x18\x1b\x1e\x1eO\\D\x02\x05\x1c\x1aC\x12\x1a\x1f\r\x19\r\x1b\x1e\x10\x01\x08\n\x02\x1b\x0b\x03\x01]\x08\n\x01@\x00\x1e\x0c\x10\x03\x00\x1a@X\x0fGF\n\x00_\x0cV\x0cFB\x0eR\\\x0e\n\x0eAG[\x07UXY\x0eBK\x08]\x0e[A\x1f\x14\x04D\x00U\x0c]\x0cL\x12\\R\x0fVZU@\x15\x0fWYZ\x0c\x0b@CX\x03\x0e_]\x0f\x10\x11\x0eP_]WUFA\nJ\n\x03\x0f\n'
key = input("Enter key: ").encode()

if len(key) != 8:
    print("ERROR! Bad key")
else:
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(good_ciphering(ciphertext[i], key[i % len(key)], 1337))
    plaintext = bytearray(plaintext).decode()
    
    # for improving security, get some secret data from internet
    r = requests.get(plaintext)
    
    flag = good_encrypting(r.text, 228)
    print(flag)
