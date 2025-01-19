from pydantic import BaseModel, Field


class HTTPExceptionResponse(BaseModel):
    detail: str = Field(..., description="Error message")
