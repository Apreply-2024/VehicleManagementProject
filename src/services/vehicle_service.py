from fastapi import HTTPException

from schemas.vehicle_schema import Vehicle

from repositories.vehicle_repository import (
    create_vehicle,
    get_all_vehicles,
    get_vehicle_by_id,
    update_vehicle,
    delete_vehicle
)


def create_vehicle_service(vehicle: Vehicle):

    return create_vehicle(vehicle)


def get_all_vehicles_service():

    return get_all_vehicles()


def get_vehicle_service(vehicle_id: int):

    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicle


def update_vehicle_service(vehicle_id: int, vehicle: Vehicle):

    updated_vehicle = update_vehicle(vehicle_id, vehicle)

    if updated_vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "message": "Vehicle updated successfully",
        "vehicle": updated_vehicle
    }


def delete_vehicle_service(vehicle_id: int):

    deleted_vehicle = delete_vehicle(vehicle_id)

    if deleted_vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "message": "Vehicle deleted successfully",
        "vehicle": deleted_vehicle
    }