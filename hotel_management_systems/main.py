from fastapi import FastAPI 
import uvicorn
from . import login
from .routers import customers,rooms,bookings,payments




app =FastAPI(
    title="Hotel Management System", 
    description="API documentation for hotel management",
    version="1.0.0",
)

app.include_router(login.router)
app.include_router(customers.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
app.include_router(payments.router)





#to start and reload server auto
def start():
    uvicorn.run("hotel_management_systems.main:app",host="127.0.0.1",port=2323,reload=True)
