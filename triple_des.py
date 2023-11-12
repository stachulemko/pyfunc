from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Avoid Option 3
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

cipher = DES3.new(key, DES3.MODE_CFB)
plaintext = b'We are no longer the knights who say ni!'
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)
