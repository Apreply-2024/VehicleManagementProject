from schemas.response_schema import APIResponse
from schemas.vehicle_schema import VehicleCreate, VehicleResponse
from repositories.vehicle_repository import search_vehicles

from exceptions.custom_exceptions import AppException
from repositories.vehicle_repository import advanced_search

from repositories.vehicle_repository import (
    create_vehicle,
    get_all_vehicles,
    get_vehicle_by_id,
    update_vehicle,
    delete_vehicle
)

from repositories.vehicle_repository import (
    get_dashboard_summary,
    get_manufacturer_distribution,
    get_status_distribution
)

from repositories.vehicle_repository import (
    get_vehicle_statistics
)

def create_vehicle_service(vehicle: VehicleCreate):

    db_vehicle = create_vehicle(vehicle)

    return APIResponse(
        success=True,
        message="Vehicle created successfully",
        data=db_vehicle
    )


def get_all_vehicles_service(
        skip: int = 0,
        limit: int = 10,
        make: str = None,
        model: str = None,
        status: str = None,
        sort_by: str = None,
        order: str = "asc"
):

    vehicles = get_all_vehicles(
    skip,
    limit,
    make,
    model,
    status,
    sort_by,
    order
)

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

def search_vehicles_service(keyword: str):

    vehicles = search_vehicles(keyword)

    return APIResponse(
        success=True,
        message="Search completed successfully",
        data=vehicles
    )

def get_vehicle_statistics_service():

    statistics = get_vehicle_statistics()

    return APIResponse(
        success=True,
        message="Statistics fetched successfully",
        data=statistics
    )

def advanced_search_service(
        make: str = None,
        model: str = None,
        vin: str = None,
        status: str = None
):

    vehicles = advanced_search(
        make,
        model,
        vin,
        status
    )

    return APIResponse(
        success=True,
        message="Advanced search completed successfully",
        data=vehicles
    )

def get_dashboard_summary_service():

    summary = get_dashboard_summary()

    return APIResponse(
        success=True,
        message="Dashboard summary fetched successfully",
        data=summary
    )


def get_status_distribution_service():

    distribution = get_status_distribution()

    return APIResponse(
        success=True,
        message="Status distribution fetched successfully",
        data={
            "distribution": distribution
        }
    )

def get_manufacturer_distribution_service():

    distribution = get_manufacturer_distribution()

    return APIResponse(
        success=True,
        message="Manufacturer distribution fetched successfully",
        data={
            "distribution": distribution
        }
    )