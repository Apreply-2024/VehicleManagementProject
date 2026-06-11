from database.database import SessionLocal
from models.vehicle_model import VehicleModel
from sqlalchemy import or_
from sqlalchemy import func

# -----------------------------
# CREATE VEHICLE
# -----------------------------
def create_vehicle(vehicle):

    db = SessionLocal()

    db_vehicle = VehicleModel(
        make=vehicle.make,
        model=vehicle.model,
        year=vehicle.year,
        vin=vehicle.vin,
        status=vehicle.status
    )

    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    db.close()

    return db_vehicle


# -----------------------------
# GET ALL VEHICLES
# -----------------------------
def get_all_vehicles(
        skip: int = 0,
        limit: int = 10,
        make: str = None,
        model: str = None,
        status: str = None,
        sort_by: str = None,
        order: str = "asc"
):

    db = SessionLocal()

    query = db.query(VehicleModel)

    if make:
        query = query.filter(
            VehicleModel.make == make
        )

    if model:
        query = query.filter(
            VehicleModel.model == model
        )

    if status:
        query = query.filter(
            VehicleModel.status == status
        )

    if sort_by:

     column = getattr(
        VehicleModel,
        sort_by,
        None
    )

    if column:

        if order.lower() == "desc":
            query = query.order_by(
                column.desc()
            )

        else:
            query = query.order_by(
                column.asc()
            )

    vehicles = (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )

    db.close()

    return vehicles


# -----------------------------
# GET VEHICLE BY ID
# -----------------------------
def get_vehicle_by_id(vehicle_id: int):

    db = SessionLocal()

    vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()

    db.close()

    return vehicle


# -----------------------------
# UPDATE VEHICLE
# -----------------------------
def update_vehicle(vehicle_id: int, vehicle):

    db = SessionLocal()

    db_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()

    if not db_vehicle:
        db.close()
        return None

    db_vehicle.make = vehicle.make
    db_vehicle.model = vehicle.model
    db_vehicle.year = vehicle.year
    db_vehicle.vin = vehicle.vin
    db_vehicle.status = vehicle.status

    db.commit()
    db.refresh(db_vehicle)

    db.close()

    return db_vehicle


# -----------------------------
# DELETE VEHICLE
# -----------------------------
def delete_vehicle(vehicle_id: int):

    db = SessionLocal()

    db_vehicle = db.query(VehicleModel).filter(VehicleModel.id == vehicle_id).first()

    if not db_vehicle:
        db.close()
        return None

    db.delete(db_vehicle)
    db.commit()

    db.close()

    return db_vehicle

def search_vehicles(keyword: str):

    db = SessionLocal()

    vehicles = (
        db.query(VehicleModel)
        .filter(
            or_(
                VehicleModel.make.contains(keyword),
                VehicleModel.model.contains(keyword),
                VehicleModel.vin.contains(keyword),
                VehicleModel.status.contains(keyword)
            )
        )
        .all()
    )

    db.close()

    return vehicles

def get_vehicle_statistics():

    db = SessionLocal()

    total_vehicles = (
        db.query(VehicleModel)
        .count()
    )

    active_vehicles = (
        db.query(VehicleModel)
        .filter(
            VehicleModel.status == "active"
        )
        .count()
    )

    inactive_vehicles = (
        db.query(VehicleModel)
        .filter(
            VehicleModel.status == "inactive"
        )
        .count()
    )

    make_counts = (
        db.query(
            VehicleModel.make,
            func.count(VehicleModel.id)
        )
        .group_by(
            VehicleModel.make
        )
        .all()
    )

    vehicles_by_make = {
        make: count
        for make, count in make_counts
    }

    db.close()

    return {
        "total_vehicles": total_vehicles,
        "active_vehicles": active_vehicles,
        "inactive_vehicles": inactive_vehicles,
        "vehicles_by_make": vehicles_by_make
    }

def advanced_search(
        make: str = None,
        model: str = None,
        vin: str = None,
        status: str = None
):

    db = SessionLocal()

    query = db.query(VehicleModel)

    if make:
        query = query.filter(
            VehicleModel.make.ilike(f"%{make}%")
        )

    if model:
        query = query.filter(
            VehicleModel.model.ilike(f"%{model}%")
        )

    if vin:
        query = query.filter(
            VehicleModel.vin.ilike(f"%{vin}%")
        )

    if status:
        query = query.filter(
            VehicleModel.status.ilike(f"%{status}%")
        )

    vehicles = query.all()

    db.close()

    return vehicles


def get_dashboard_summary():

    db = SessionLocal()

    total = db.query(VehicleModel).count()

    active = (
        db.query(VehicleModel)
        .filter(
            VehicleModel.status == "active"
        )
        .count()
    )

    inactive = (
        db.query(VehicleModel)
        .filter(
            VehicleModel.status == "inactive"
        )
        .count()
    )

    db.close()

    return {
        "total_vehicles": total,
        "active_vehicles": active,
        "inactive_vehicles": inactive
    }

def get_manufacturer_distribution():

    db = SessionLocal()

    result = (
        db.query(
            VehicleModel.make,
            func.count(VehicleModel.id)
        )
        .group_by(
            VehicleModel.make
        )
        .all()
    )

    db.close()

    return {
        make: count
        for make, count in result
    }


def get_status_distribution():

    db = SessionLocal()

    result = (
        db.query(
            VehicleModel.status,
            func.count(VehicleModel.id)
        )
        .group_by(
            VehicleModel.status
        )
        .all()
    )

    db.close()

    return {
        status: count
        for status, count in result
    }
