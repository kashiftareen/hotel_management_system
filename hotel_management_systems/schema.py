from pydantic import BaseModel
from enum import Enum

# define RoomStatus Enum
class RoomStatus(Enum):
    available="available"
    booked = "booked"