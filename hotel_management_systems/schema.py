from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import date

# define RoomStatus Enum
class RoomStatus(Enum):
    available="available"
    booked = "booked"

#Customer Schema
class Create_User(BaseModel):
    username:str
    email:str
    password:str
    phone:str
# Schema for updating customer details
class update_cust(Create_User):
    pass

# To create Room Schema
class create_room(BaseModel):
    number:str
    price:float
    status:RoomStatus
# Schema for updating room details
class update_room(BaseModel):
    number: Optional[str] = None
    price: Optional[float] = None
    status: Optional[RoomStatus] = None

# Booking Schema
class create_booking(BaseModel):
    customer_id:int
    room_id :int
    check_in:date
    check_out:date
    status:Optional[str]="pending"

# Schema for updating booking details
class update_booking(BaseModel):
    check_in:date
    check_out:date
    status:Optional[str]="pending"

#create_payment schmea
class create_payment(BaseModel):
    booking_id:int
    amount:float
    method:str

# Schema shows customers
class show_customers(BaseModel):
    id:int
    username:str
    email:str
    phone:str

    class Config:
        orm_mode = True

# to register new user schema
class new_user(show_customers):
    pass
