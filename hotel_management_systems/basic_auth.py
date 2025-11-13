from jose import jwt,JWTError
from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from .utils import settings
from datetime import datetime ,timedelta
from . import models,schema,database

# Access environment variables
dburi=settings.dburi
secret_key=settings.secret_key
algorithm=settings.algorithm
access_token_expire_minutes=settings.access_token_expire_minutes

oauth2_schema =OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    # create a copy of given dictionary
    to_encode = data.copy()
    #set expiry time of token
    expiry = datetime.utcnow()+timedelta(minutes=access_token_expire_minutes)
    # Add expiry in token
    to_encode.update({"exp":expiry})
    #create jwt token
    jwt_token = jwt.encode(to_encode,secret_key,algorithm=algorithm)
    return jwt_token

#verift the token and return the loged in user from database
def verify_access_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        # Fetch the user object from the database
        user = db.query(models.Customers).filter(models.Customers.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user  # return the user object
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


def get_current_user(token: str = Depends(oauth2_schema),
                     db: Session = Depends(database.get_db)):
    return verify_access_token(token, db)
