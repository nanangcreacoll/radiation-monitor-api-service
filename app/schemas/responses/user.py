from pydantic import BaseModel, Field


class UserLoginResponse(BaseModel):
    type: str = Field(..., description="Authentication type")
    token: str = Field(..., description="Authentication token")


class UserRegisterResponse(BaseModel):
    id: int = Field(..., description="ID of the user")
    username: str = Field(..., description="Username of the user")
