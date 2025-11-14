from fastapi import APIRouter,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from .. import database,models,schema

router=APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

#create_payments
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_payment(payments:schema.create_payment,db:Session=Depends(database.get_db)):
    create = models.Payments(**payments.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

# list of payments
@router.get("/",status_code=status.HTTP_200_OK)
def list_of_payments(db:Session=Depends(database.get_db)):
    get = db.query(models.Payments).all()
    if get is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="empty list"
        )
    return get

# get single payment with booking_id
@router.get("/{id}",status_code=status.HTTP_200_OK)
def payment_by_id(id:int,db:Session=Depends(database.get_db)):
    get_by_id =db.query(models.Payments).filter(models.Payments.id == id).first()
    if get_by_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"payment with this given id {id} is not founded."
        ) 
    return get_by_id