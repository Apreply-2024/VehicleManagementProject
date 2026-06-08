from fastapi import APIRouter, status

from schemas.vehicle_schema import Vehicle

from services.vehicle_service import (
    create_vehicle_service,
    get_all_vehicles_service,
    get_vehicle_service,
    update_vehicle_service,
    delete_vehicle_service
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Vehicles"]
)


@router.post(
    "/vehicles",
    status_code=status.HTTP_201_CREATED
)
def create_vehicle(vehicle: Vehicle):

    return {
        "message": "Vehicle added successfully",
        "vehicle": create_vehicle_service(vehicle)
    }


@router.get("/vehicles")
def get_vehicles():

    return get_all_vehicles_service()


@router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    return get_vehicle_service(vehicle_id)


@router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: Vehicle):

    return update_vehicle_service(vehicle_id, vehicle)


@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):

    return delete_vehicle_service(vehicle_id)