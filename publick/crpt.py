'''
the Encrypt and Decrypt method
'''
import bcrypt


class Crypt:
    @classmethod
    def encrypt(cls,passwd):
        salt = bcrypt.gensalt(12)
        return bcrypt.hashpw(passwd.encode(),salt)
    
    @classmethod
    def decrypt(cls,passwd,hashed_password):
        return bcrypt.checkpw(passwd.encode(),hashed_password)

