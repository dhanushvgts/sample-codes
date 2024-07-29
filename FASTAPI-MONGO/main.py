from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routes.route import router

app=FastAPI()

app.include_router(router)



