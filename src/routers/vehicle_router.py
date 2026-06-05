from fastapi import APIRouter, HTTPException
from schemas.vehicle_schema import Vehicle

router = APIRouter()

vehicles = []


@router.post("/vehicles")
def create_vehicle(vehicle: Vehicle):

    vehicles.append(vehicle)

    return {
        "message": "Vehicle added successfully",
        "vehicle": vehicle
    }

@router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    if vehicle_id >= len(vehicles):
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicles[vehicle_id]

@router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    return vehicles[vehicle_id]