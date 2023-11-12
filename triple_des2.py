from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Random import get_random_bytes
key = key = DES3.adjust_key_parity(get_random_bytes(24))
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = ' kupa ma kota   ' #padded with spaces so than len(plaintext) is multiple of 8
encrypted_text = cipher_encrypt.encrypt(plaintext)

cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
cipher_decrypt.decrypt(encrypted_text)
cipher_decrypt.decrypt(encrypted_text) #you cant do it twice
