from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

salt = b'+\x8e\x15\x00\x1c\x13\xff\xf4T\xdb4\xfb\xd3\x0f6q'
PW = PBKDF2("testpassword", salt, dkLen=16)
# PW = "testpassword"
BS = 16
def encrypt_func():
    with open("encrypt.txt", 'rb') as f:
        cipher = AES.new(PW, AES.MODE_CBC)
        cipher_file = cipher.encrypt(pad(f.read(), BS))
        print(cipher_file)
        print(cipher.iv)
    with open("encrypt.txt", 'wb') as f:
        f.write(cipher.iv)
        f.write(cipher_file)

def decrypt_func():
    with open("encrypt.txt", 'rb') as f:
        iv = f.read(16) # 16bit
        decrypt_file = f.read()
    print(iv)
    print(decrypt_file)
    cipher = AES.new(PW, AES.MODE_CBC, IV=iv)
    # print(cipher.decrypt(decrypt_file))
    og_file = unpad(cipher.decrypt(decrypt_file), BS)
    print(og_file)

    with open("encrypt.txt", 'wb') as f:
        f.write(og_file)

if __name__ == '__main__':
    # print(PW)
    # encrypt_func()
    # decrypt_func()
    os.chmod('encrypt.txt', 0000)
    print(oct(os.stat('encrypt.txt').st_mode))
    # b'k\xa2f\xbd\x840>\x16vb\x8cR\xa0\xd3\xbf\xf7'