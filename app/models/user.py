from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    password: str
    created_at: str
    updated_at: Optional[str] = None
