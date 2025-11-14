from pydantic import BaseModel
from enum import Enum
from typing import Optional

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

class update_room(BaseModel):
    number: Optional[str] = None
    price: Optional[float] = None
    status: Optional[RoomStatus] = None