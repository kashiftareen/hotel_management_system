from fastapi import Depends,HTTPException,status,Response,APIRouter
from sqlalchemy.orm import Session
from .. import database,schema,models,basic_auth
from sqlalchemy import func

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)



"""Return hotel statistics such as:
    Total rooms
    Total bookings
    Total customers
    Total revenue (sum of all payments)"""
@router.get("/summary",status_code=status.HTTP_200_OK)
def get_summary(db:Session=Depends(database.get_db),
                current_user:models.Customers=Depends(basic_auth.get_current_user)):
    total_rooms = db.query(func.count(models.Room.id)).scalar()
    total_customers = db.query(func.count(models.Customers.id)).scalar()
    total_bookings = db.query(func.count(models.Bookings.id)).scalar()
    total_payments = db.query(func.coalesce(func.sum(models.Payments.amount)),0).scalar()
    
    return {
        "total_rooms": total_rooms,
        "total_customers": total_customers,
        "total_bookings": total_bookings,
        "total_revenue": total_payments
    }