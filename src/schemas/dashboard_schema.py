from typing import Dict
from pydantic import BaseModel


class DashboardSummary(BaseModel):

    total_vehicles: int
    active_vehicles: int
    inactive_vehicles: int


class DashboardDistribution(BaseModel):

    distribution: Dict[str, int]