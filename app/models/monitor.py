from pydantic import BaseModel
import datetime


class Monitor(BaseModel):
    id: int
    user_id: int
    temperature: float
    humidity: float
    dose_rate: float
    created_at: datetime.datetime
