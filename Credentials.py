from passlib.context import CryptContext

crypt_pass = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_pass(password: str):
    return crypt_pass.hash(password)

def Verify_Pass(plain_pass,Generated_pass):
    return crypt_pass.verify(plain_pass,Generated_pass)