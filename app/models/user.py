from pydantic import BaseModel
from typing import Optional
import datetime


class User(BaseModel):
    id: int
    username: str
    password: str
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None
