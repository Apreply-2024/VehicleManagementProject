from fastapi import FastAPI

from database.database import engine
from models.vehicle_model import VehicleModel
from routers.vehicle_router import router

from exceptions.custom_exceptions import AppException
from exceptions.exception_handler import app_exception_handler


VehicleModel.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vehicle Management System API",
    version="1.0.0"
)

app.add_exception_handler(AppException, app_exception_handler)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Vehicle Management System"
    }