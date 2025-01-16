from pydantic import BaseModel
from typing import Optional


class PersonalAccessToken(BaseModel):
    id: int
    user_id: int
    token: str
    created_at: str
    last_used_at: Optional[str] = None
    updated_at: Optional[str] = None
