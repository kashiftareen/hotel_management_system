from fastapi import Depends,HTTPException,status,Response,APIRouter
from sqlalchemy.orm import Session
from .. import database,schema,models,basic_auth

router = APIRouter(
    tags=["Customer_Bookings"]
)

#list of customer_bookings
@router.get("/customer_bookings{id}",status_code=status.HTTP_200_OK)
def bookings(id:int,db:Session=Depends(database.get_db),
             current_user:models.Customers=Depends(basic_auth.get_current_user)):
    customer = db.query(models.Customers).filter(models.Customers.id == id).first()
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    list_bookings= db.query(models.Bookings).filter(models.Bookings.customer_id == id).all()
    if list_bookings is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return list_bookings

#List of customer_payments
@router.get("/get_booking_payment{id}",status_code=status.HTTP_200_OK)
def payment_list(id:int,db:Session=Depends(database.get_db),
                 current_user:models.Customers=Depends(basic_auth.get_current_user)):
    booking = db.query(models.Bookings).filter(models.Bookings.id == id).first()
    if booking is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    payment = db.query(models.Payments).filter(models.Payments.booking_id == id).all()
    if payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return payment
