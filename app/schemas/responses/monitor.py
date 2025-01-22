from pydantic import BaseModel, Field
import datetime


class MonitorResponse(BaseModel):
    id: int = Field(..., description="ID of the monitor data")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., description="Relative humidity in percentage")
    dose_rate: float = Field(..., description="Dose rate in microsieverts per hour")
    created_at: datetime.datetime = Field(
        ..., description="Date and time of monitor data creation"
    )
