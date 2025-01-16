from pydantic import BaseModel, Field, field_validator
import re

re_username = re.compile(r"^[a-zA-Z0-9]+$")
re_password = re.compile(r"^[a-zA-Z0-9]+$")


class UserLogin(BaseModel):
    username: str = Field(..., description="Username of the user", max_length=255)
    password: str = Field(..., description="Password of the user", max_length=255)

    @field_validator("username")
    def validate_username(cls, value):
        if not re_username.fullmatch(value):
            raise ValueError(
                "Username must contain only alphabets and numbers without spaces."
            )
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if not re_password.fullmatch(value):
            raise ValueError(
                "Password must contain only alphabets and numbers without spaces."
            )
        return value


class UserRegister(BaseModel):
    username: str = Field(..., description="Username of the user", max_length=255)
    password: str = Field(..., description="Password of the user", max_length=255)

    @field_validator("username")
    def validate_username(cls, value):
        if not re_username.fullmatch(value):
            raise ValueError(
                "Username must contain only alphabets and numbers without spaces."
            )
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if not re_password.fullmatch(value):
            raise ValueError(
                "Password must contain only alphabets and numbers without spaces."
            )
        return value
