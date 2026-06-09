from fastapi import FastAPI
from database.database import engine
from models.vehicle_model import VehicleModel
from routers.vehicle_router import router

VehicleModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Vehicle Management System"
    }