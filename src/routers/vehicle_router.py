from typing import List

from fastapi import APIRouter

from schemas.vehicle_schema import VehicleCreate, VehicleResponse
from schemas.response_schema import APIResponse

from services import vehicle_service


router = APIRouter(
    prefix="/api/v1",
    tags=["Vehicles"]
)


@router.post(
    "/vehicles",
    response_model=APIResponse[VehicleResponse],
    summary="Create a vehicle",
    description="Creates a new vehicle in the database."
)
def create_vehicle(vehicle: VehicleCreate):

    return vehicle_service.create_vehicle_service(vehicle)


@router.get(
    "/vehicles",
    response_model=APIResponse[List[VehicleResponse]],
    summary="Get all vehicles",
    description="Returns all vehicles from the database."
)
def get_vehicles():

    return vehicle_service.get_all_vehicles_service()


@router.get(
    "/vehicles/{vehicle_id}",
    response_model=APIResponse[VehicleResponse],
    summary="Get vehicle by ID",
    description="Retrieves a vehicle using its ID."
)
def get_vehicle(vehicle_id: int):

    return vehicle_service.get_vehicle_service(vehicle_id)


@router.put(
    "/vehicles/{vehicle_id}",
    response_model=APIResponse[VehicleResponse],
    summary="Update a vehicle",
    description="Updates an existing vehicle."
)
def update_vehicle(vehicle_id: int, vehicle: VehicleCreate):

    return vehicle_service.update_vehicle_service(vehicle_id, vehicle)


@router.delete(
    "/vehicles/{vehicle_id}",
    response_model=APIResponse[VehicleResponse],
    summary="Delete a vehicle",
    description="Deletes a vehicle from the database."
)
def delete_vehicle(vehicle_id: int):

    return vehicle_service.delete_vehicle_service(vehicle_id)