from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,HTTPException,status,Response
from .. import database,models,schema

router=APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

# Create BOOKING of a room 
@router.post("/",status_code=status.HTTP_200_OK)
def create_booking(booking:schema.create_booking,db:Session=Depends(database.get_db)):
    create = models.Bookings(**booking.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

#get list of bookings 
@router.get("/",status_code=status.HTTP_200_OK)
def get_bookings_list(db:Session=Depends(database.get_db)):
    get = db.query(models.Bookings).all()
    if get is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return get

# Get one Booking
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_singel_booking(id:int,db:Session=Depends(database.get_db)):
    get = db.query(models.Bookings).filter(models.Bookings.id == id).first()
    if get is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return get


# Update Booking
@router.put("/{id}",status_code=status.HTTP_200_OK)
def update_booking(id:int,update_bkg:schema.update_booking,db:Session=Depends(database.get_db)):
    update = db.query(models.Bookings).filter(models.Bookings.id == id).first()
    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    for keys,values in update_bkg.dict(exclude_unset=True).items():
        setattr(update,keys,values)
    db.commit()
    db.refresh(update)
    return update

#Delete or cancel booking
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(id:int,db:Session=Depends(database.get_db)):
    del_bkg = db.query(models.Bookings).filter(models.Bookings.id == id).first()
    if del_bkg is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"booking with given id {id} is not founded."
        )
    db.delete(del_bkg)
    db.commit()
    return #No response body for 204