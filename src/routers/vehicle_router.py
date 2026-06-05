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

    if vehicle_id < 0 or vehicle_id >= len(vehicles):
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicles[vehicle_id]

@router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: Vehicle):

    if vehicle_id < 0 or vehicle_id >= len(vehicles):
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    vehicles[vehicle_id] = vehicle

    return {
        "message": "Vehicle updated successfully",
        "vehicle": vehicle
    }

@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):

    if vehicle_id < 0 or vehicle_id >= len(vehicles):
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    deleted_vehicle = vehicles.pop(vehicle_id)

    return {
        "message": "Vehicle deleted successfully",
        "vehicle": deleted_vehicle
    }

@router.get("/vehicles")
def get_vehicles():

    return vehicles