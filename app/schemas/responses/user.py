from pydantic import BaseModel, Field
from typing import Optional
import datetime


class User(BaseModel):
    id: int
    username: str
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None


class UserLoginResponse(BaseModel):
    type: str = Field(..., description="Authentication type")
    token: str = Field(..., description="Authentication token")


class UserRegisterResponse(BaseModel):
    id: int = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
