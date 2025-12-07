from fastapi import Depends
from sqlalchemy import Column,String,Integer,Boolean,Enum as sqlenum,ForeignKey,Date,Float
from sqlalchemy.orm import declarative_base,relationship
from datetime import datetime
from .schema import RoomStatus


Base=declarative_base()


#Customer Table
class Customers(Base):
    __tablename__ ="customers"
    id =Column(Integer,nullable=False,primary_key=True,index=True)
    username =Column(String,nullable=False)
    email =Column(String,nullable=False,unique=True)
    password= Column(String(100))
    phone =Column(String)
    #relationship
    bookings=relationship("Bookings",back_populates="customer")

#Room Table
class Room(Base):
    __tablename__ ="rooms"
    id=Column(Integer,nullable=False,primary_key=True,index=True)
    number=Column(String,unique=True)
    price =Column(Float)
    status=Column(sqlenum(RoomStatus),default=RoomStatus.available)
    #Relationship
    bookings =relationship("Bookings",back_populates="room")

#Booking Table
class Bookings(Base):
    __tablename__ = "bookings"
    id=Column(Integer,nullable=False,primary_key=True,index=True)
    customer_id=Column(Integer,ForeignKey("customers.id"))
    room_id =Column(Integer,ForeignKey("rooms.id"))
    check_in=Column(Date, default=lambda: datetime.utcnow().date())
    check_out=Column(Date)
    status=Column(String)
    #Relationship
    customer=relationship("Customers",back_populates="bookings")
    room=relationship("Room",back_populates="bookings")
    payment=relationship("Payments",back_populates="bookings",uselist=False)

#Payments Table
class Payments(Base):
    __tablename__="payments"
    id =Column(Integer,nullable=False,primary_key=True,index=True)
    booking_id=Column(Integer,ForeignKey("bookings.id"))
    amount=Column(Float)
    method=Column(String)
    #Relationship
    bookings=relationship("Bookings",back_populates="payment")

    #end of models.py

    


