from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router

#Initialize main app
app=FastAPI()
#include created routers to main file
app.include_router(auth_router)
app.include_router(order_router)