from fastapi import APIRouter,Depends,Response,status,HTTPException
from sqlalchemy.orm import Session
from . import models,schema,basic_auth,database,hash
from fastapi.security import OAuth2PasswordRequestForm



router=APIRouter(
    tags=["User_Login"]
)
#register  a new custmer with hash password in database
@router.post("/register",status_code=status.HTTP_201_CREATED,response_model=schema.new_user)
def register_user(user:schema.Create_User,db:Session=Depends(database.get_db)):
    existing = db.query(models.Customers).filter(
        (models.Customers.username == user.username)|
        (models.Customers.email == user.email)).first()
    if existing :
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Username already Existing."
        )
    hash_pwd =hash.hash_pwd(user.password)
    add = models.Customers(
        username=user.username,
        email=user.email,
        password=hash_pwd,
        phone=user.phone
        )
    db.add(add)
    db.commit()
    db.refresh(add)
    return add



# Login /authentication
@router.post("/login",status_code=status.HTTP_200_OK)
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