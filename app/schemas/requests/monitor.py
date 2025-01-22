from pydantic import BaseModel, Field


class MonitorRequest(BaseModel):
    temperature: float = Field(
        ..., description="Temperature in Celsius", ge=-100, le=100
    )
    humidity: float = Field(
        ..., description="Relative humidity in percentage", ge=0, le=100
    )
    dose_rate: float = Field(
        ..., description="Dose rate in microsieverts per hour", ge=0, le=1000000
    )
