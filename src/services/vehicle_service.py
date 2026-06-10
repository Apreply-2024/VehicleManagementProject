from schemas.response_schema import APIResponse
from schemas.vehicle_schema import VehicleCreate, VehicleResponse

from exceptions.custom_exceptions import AppException

from repositories.vehicle_repository import (
    create_vehicle,
    get_all_vehicles,
    get_vehicle_by_id,
    update_vehicle,
    delete_vehicle
)


def create_vehicle_service(vehicle: VehicleCreate):

    db_vehicle = create_vehicle(vehicle)

    return APIResponse(
        success=True,
        message="Vehicle created successfully",
        data=db_vehicle
    )


def get_all_vehicles_service():

    vehicles = get_all_vehicles()

    return APIResponse(
        success=True,
        message="Vehicles fetched successfully",
        data=vehicles
    )


def get_vehicle_service(vehicle_id: int):

    vehicle = get_vehicle_by_id(vehicle_id)

    if not vehicle:
        raise AppException("Vehicle not found", 404)

    return APIResponse(
        success=True,
        message="Vehicle fetched successfully",
        data=vehicle
    )


def update_vehicle_service(vehicle_id: int, vehicle: VehicleCreate):

    updated_vehicle = update_vehicle(vehicle_id, vehicle)

    if not updated_vehicle:
        raise AppException("Vehicle not found", 404)

    return APIResponse(
        success=True,
        message="Vehicle updated successfully",
        data=updated_vehicle
    )


def delete_vehicle_service(vehicle_id: int):

    deleted_vehicle = delete_vehicle(vehicle_id)

    if not deleted_vehicle:
        raise AppException("Vehicle not found", 404)

    return APIResponse(
        success=True,
        message="Vehicle deleted successfully",
        data=deleted_vehicle
    )