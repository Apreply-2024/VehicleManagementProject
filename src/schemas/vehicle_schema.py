from typing import Literal

from pydantic import BaseModel, Field


class VehicleCreate(BaseModel):

    make: str = Field(
        min_length=2,
        max_length=50,
        description="Vehicle manufacturer name",
        examples=["Toyota"]
    )

    model: str = Field(
        min_length=1,
        max_length=50,
        description="Vehicle model name",
        examples=["Camry"]
    )

    year: int = Field(
        ge=1900,
        le=2100,
        description="Manufacturing year",
        examples=[2022]
    )

    vin: str = Field(
        min_length=5,
        max_length=30,
        description="Unique vehicle VIN number",
        examples=["VIN001"]
    )

    status: Literal[
        "active",
        "inactive",
        "maintenance"
    ]


class VehicleResponse(BaseModel):

    id: int
    make: str
    model: str
    year: int
    vin: str
    status: str

    class Config:
        from_attributes = True