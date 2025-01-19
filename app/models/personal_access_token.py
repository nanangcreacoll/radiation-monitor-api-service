from pydantic import BaseModel
from typing import Optional
import datetime


class PersonalAccessToken(BaseModel):
    id: int
    user_id: int
    token: str
    created_at: datetime.datetime
    last_used_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
