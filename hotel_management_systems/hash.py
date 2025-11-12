from passlib.context import  CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# To hashed simple password
def hash_pwd(password:str):
    return pwd_context.hash(password)

# Tp verify hash password
def verify_pwd(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)