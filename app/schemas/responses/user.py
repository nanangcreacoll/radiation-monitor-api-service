from pydantic import BaseModel, Field
from typing import Optional
import datetime


class User(BaseModel):
    id: int = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
    created_at: datetime.datetime = Field(
        ..., description="Date and time of user creation"
    )
    updated_at: Optional[datetime.datetime] = Field(
        None, description="Date and time of user update"
    )


class UserLoginResponse(BaseModel):
    type: str = Field(..., description="Authentication type")
    token: str = Field(..., description="Authentication token")


class UserRegisterResponse(BaseModel):
    id: int = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
