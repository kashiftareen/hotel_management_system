from fastapi import FastAPI 
import uvicorn




app =FastAPI(
    title="Hotel Management System", 
    description="API documentation for hotel management",
    version="1.0.0",
)






#to start and reload server auto
def start():
    uvicorn.run("hotel_management_system.main:app",host="127.0.0.1",port=2323,reload=True)
    