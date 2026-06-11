from pydantic import BaseModel
from typing import Dict


class VehicleStatistics(BaseModel):

    total_vehicles: int
    active_vehicles: int
    inactive_vehicles: int
    vehicles_by_make: Dict[str, int]

