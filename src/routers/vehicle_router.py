from typing import List

from fastapi import APIRouter
from fastapi import Query

from schemas.vehicle_schema import VehicleCreate, VehicleResponse
from schemas.response_schema import APIResponse

from services import vehicle_service
from schemas.statistics_schema import VehicleStatistics

from schemas.dashboard_schema import (
    DashboardSummary,
    DashboardDistribution
)

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
def get_vehicles(

        skip: int = Query(
            default=0,
            ge=0
        ),

        limit: int = Query(
            default=10,
            ge=1,
            le=100
        ),

        make: str = None,

        model: str = None,

        status: str = None,

        sort_by: str = None,

        order: str = Query(
            default="asc"
        )
):

    return vehicle_service.get_all_vehicles_service(
    skip,
    limit,
    make,
    model,
    status,
    sort_by,
    order
    )

@router.get(
    "/vehicles/search",
    response_model=APIResponse[List[VehicleResponse]],
    summary="Search vehicles",
    description="Search vehicles by make, model, VIN, or status."
)
def search_vehicle(

        keyword: str = Query(
            ...,
            min_length=1
        )
):

    return vehicle_service.search_vehicles_service(keyword)

@router.get(
    "/vehicles/statistics",
    response_model=APIResponse[VehicleStatistics],
    summary="Vehicle statistics",
    description="Returns dashboard statistics."
)
def get_statistics():

    return vehicle_service.get_vehicle_statistics_service()

@router.get(
    "/vehicles/advanced-search",
    response_model=APIResponse[List[VehicleResponse]],
    summary="Advanced search",
    description="Search vehicles using make, model, vin and status."
)
def advanced_search(

        make: str = None,
        model: str = None,
        vin: str = None,
        status: str = None
):

    return vehicle_service.advanced_search_service(
        make,
        model,
        vin,
        status
    )

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


@router.get(
    "/dashboard/summary",
    response_model=APIResponse[DashboardSummary]
)
def dashboard_summary():

    return vehicle_service.get_dashboard_summary_service()


@router.get(
    "/dashboard/manufacturers",
    response_model=APIResponse[DashboardDistribution]
)
def dashboard_manufacturers():

    return vehicle_service.get_manufacturer_distribution_service()


@router.get(
    "/dashboard/status-distribution",
    response_model=APIResponse[DashboardDistribution]
)
def dashboard_status_distribution():

    return vehicle_service.get_status_distribution_service()

