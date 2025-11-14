from fastapi import Depends,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from .. import database,schema,models,basic_auth

router=APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)
#Create room 
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_room(room:schema.create_room,db:Session=Depends(database.get_db),
                current_user:models.Customers=Depends(basic_auth.get_current_user)):
    rooms = models.Room(**room.dict())
    #save in database
    db.add(rooms)
    db.commit()
    db.refresh(rooms)
    return rooms

#get list of rooms 
@router.get("/",status_code=status.HTTP_200_OK)
def get_list(db:Session=Depends(database.get_db),
             current_user:models.Customers=Depends(basic_auth.get_current_user)):
    rooms = db.query(models.Room).all()
    if rooms is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return rooms

#get single room from list
@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_single(id:int,db:Session=Depends(database.get_db),
               current_user:models.Customers=Depends(basic_auth.get_current_user)):
    single_room = db.query(models.Room).filter(models.Room.id == id).first()
    if single_room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"room with this given id {id} not founded"
        )
    return single_room

@router.put("/{id}",status_code=status.HTTP_200_OK)
def update_room(id:int,room:schema.update_room,db:Session=Depends(database.get_db),
                current_user:models.Customers=Depends(basic_auth.get_current_user)):
    existing = db.query(models.Room).filter(models.Room.id == id).first()
    if existing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"room with this give id {id} is not found"
        )
    for keys,values in room.dict(exclude_unset=True).items():
        setattr(existing,keys,values)

    db.commit()
    db.refresh(existing)
    return existing

#Delete room form database
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int,db:Session=Depends(database.get_db),
           current_user:models.Customers=Depends(basic_auth.get_current_user)):
    room = db.query(models.Room).filter(models.Room.id == id).first()
    if room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Room with id {id} not found"
        )
    db.delete(room)
    db.commit()
    return #No response body for 204
