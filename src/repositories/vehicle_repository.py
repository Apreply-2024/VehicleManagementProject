from schemas.vehicle_schema import Vehicle

vehicles = []


def create_vehicle(vehicle: Vehicle):

    vehicles.append(vehicle)

    return vehicle


def get_all_vehicles():

    return vehicles


def get_vehicle_by_id(vehicle_id: int):

    if vehicle_id < 0 or vehicle_id >= len(vehicles):
        return None

    return vehicles[vehicle_id]


def update_vehicle(vehicle_id: int, vehicle: Vehicle):

    if vehicle_id < 0 or vehicle_id >= len(vehicles):
        return None

    vehicles[vehicle_id] = vehicle

    return vehicle


def delete_vehicle(vehicle_id: int):

    if vehicle_id < 0 or vehicle_id >= len(vehicles):
        return None

    return vehicles.pop(vehicle_id)