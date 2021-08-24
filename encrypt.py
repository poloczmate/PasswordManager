import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
# helykitoltes = padding
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).digest()  # password sha256 hash = private key


def encrypt(raw, private_key):
    raw = pad(raw)  # pad
    raw = str.encode(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)  # Cipher-Block Chaining mode
    return base64.b64encode(iv + cipher.encrypt(raw))  # convert bytes to characters


def decrypt(enc, private_key):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    key = unpad(cipher.decrypt(enc[16:]))
    return bytes.decode(key)
