import base64
import sys
from Crypto.Cipher import AES
from .SecurityException import SecurityException


class Encrypter:

    def __init__(self, key, salt=None):
        self.key = key.encode('utf-8')
        self.salt = b'9e1800eb5f206888' if salt is None else salt.encode('utf-8')

    def encrypt(self, plaintext):
        if plaintext == "":
            raise SecurityException("Text to be encyrpted is empty")
        try:
            aes = AES.new(self.key, AES.MODE_EAX, self.salt)
            enc = aes.encrypt(plaintext.encode('utf-8'))
            return base64.b64encode(enc).decode("utf-8")
        except Exception as e:
            raise SecurityException(str(e))

    def decrypt(self, encrypted):
        if encrypted == "":
            raise SecurityException("Text to be decrypted is empty")
        try:
            enc = base64.b64decode(encrypted.encode("utf-8"))
            aes = AES.new(self.key, AES.MODE_EAX, self.salt)
            return aes.decrypt(enc).decode("utf-8")
        except Exception:
            raise SecurityException("Could not decrypt.").with_traceback(sys.exc_info()[2])