from database.database import SessionLocal
from models.vehicle_model import VehicleModel


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
def get_all_vehicles():

    db = SessionLocal()

    vehicles = db.query(VehicleModel).all()

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