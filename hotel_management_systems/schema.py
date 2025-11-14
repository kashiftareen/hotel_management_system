from pydantic import BaseModel
from enum import Enum

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