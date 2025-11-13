from fastapi import APIRouter,Depends,Response,status,HTTPException
from sqlalchemy.orm import Session
from . import models,schema,basic_auth,database,hash
from fastapi.security import OAuth2PasswordRequestForm



router=APIRouter(
    prefix="/login",
    tags=["User_Login"]
)
# Login /authentication
@router.post("/",status_code=status.HTTP_200_OK)
def login(creds:OAuth2PasswordRequestForm=Depends(),
          db:Session=Depends(database.get_db)):
       user = db.query(models.Customers).filter(models.Customers.username == creds.username).first()
       if not user or not hash.verify_pwd(creds.password,user.password):
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                               detail="Invalid credentials")
       access_token=basic_auth.create_access_token(data={"user_id":user.id})
       return {
        "access_token":access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone
        }
        }        

#end of login.py