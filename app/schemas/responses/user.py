from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    type: str = Field(..., description="Authentication type")
    token: str = Field(..., description="Authentication token")


class UserRegister(BaseModel):
    id: int = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
