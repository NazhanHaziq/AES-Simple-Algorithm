# Ahmad Nazhan Haziq bin Ahmad Fuad (CA21060)
# Muhammad Nur Aiman bin Ali (CA21062)
# Title: Attaining Confidentiality and Authentication by Employing AES Algorithm
# Run on Python 3.12 with PyCharm IDE
# Installed "py -m pip install pycryptodome" in cmd which directory to the "C:\Users\nazhan\PycharmProjects\AES Crypto Project"

import base64
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes


### Function ###
#----------------- Encryption -----------------#
def encrypt(plaintext, key, hmac_key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pad_len = 16 - len(plaintext) % 16
    padded_plaintext = plaintext + bytes([pad_len] * pad_len)
    ciphertext = cipher.encrypt(padded_plaintext)
    iv_ciphertext = iv + ciphertext
    hmac = HMAC.new(hmac_key, iv_ciphertext, digestmod=SHA256).digest()
    encrypted_message = hmac + iv_ciphertext
    return base64.b64encode(encrypted_message)

#----------------- Decryption -----------------#
def decrypt(encrypted_message, key, hmac_key):
    encrypted_message = base64.b64decode(encrypted_message)
    hmac = encrypted_message[:32]
    iv = encrypted_message[32:48]
    ciphertext = encrypted_message[48:]
    hmac_calculated = HMAC.new(hmac_key, iv + ciphertext, digestmod=SHA256).digest()
    if hmac != hmac_calculated:
        return "Authentication failed"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    pad_len = padded_plaintext[-1]
    plaintext = padded_plaintext[:-pad_len]
    return plaintext

### Main ###
#------------------- Usage --------------------#
key = get_random_bytes(16)
hmac_key = get_random_bytes(16)

#------------------- Input --------------------#
plaintext = input("Enter the message you want to encrypt: ").encode()


#------------------- Output -------------------#
encrypted_message = encrypt(plaintext, key, hmac_key)
print(f"Encrypted: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, key, hmac_key)
print(f"Decrypted: {decrypted_message}")
