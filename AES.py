#(AES - Advanced Encryption Standard)

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(plain_text, secret_key):
   
    plain_bytes = plain_text.encode('utf-8')
    key_bytes = secret_key.encode('utf-8')
     
    iv = os.urandom(16)
    
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    padded_data = pad(plain_bytes, AES.block_size)
    cipher_text = cipher.encrypt(padded_data)
     
    return iv + cipher_text

def decrypt_aes(cipher_data, secret_key):
    key_bytes = secret_key.encode('utf-8')
    
 
    iv = cipher_data[:16]
    actual_cipher_text = cipher_data[16:]
    
    # Create AES cipher object for decryption
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    
    # Decrypt the data
    decrypted_padded = cipher.decrypt(actual_cipher_text)
    
    # Remove padding
    plain_bytes = unpad(decrypted_padded, AES.block_size)
    
    return plain_bytes.decode('utf-8')


if __name__ == "__main__":
   
    my_key = "ahmedsayedshehat" 
    message = "I'm Ahmed Sayed, Network & Cyber Security Student 🛡️🌐"
    
    print(f"Original Text: {message}")
    
    # Encryption process
    encrypted_result = encrypt_aes(message, my_key)
    print(f"Encrypted Text (Hex): {encrypted_result.hex()}")

    print("_________________________________________________________________________\n")

    # Decryption process
    decrypted_result = decrypt_aes(encrypted_result, my_key)
    print(f"Decrypted Text: {decrypted_result}")


#Original Text: I'm Ahmed Sayed, Network & Cyber Security Student 🛡️🌐
#Encrypted Text (Hex): 8b8a9c2b41776bdcd2d5b8df43c6fb133d05eaf193c4859004
# 20a96c9bdf3af333c4396fc5035e1867977882aa1f596e844775cccf0bc909ced8cb580d792d9748fe1d7b0874773a60d34100b7e2d47a
_________________________________________________________________________

#Decrypted Text: I'm Ahmed Sayed, Network & Cyber Security Student 🛡️🌐
