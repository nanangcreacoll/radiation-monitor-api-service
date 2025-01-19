from app.controllers.user import UserController
from app.schemas.responses.user import User
from app.schemas.requests.user import UserRegisterRequest
from app.schemas.responses.user import UserRegisterResponse
from app.schemas.requests.user import UserLoginRequest
from app.schemas.responses.user import UserLoginResponse

from fastapi import Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

router = APIRouter()

security = HTTPBearer()


@router.post(
    path="/user",
    status_code=201,
    response_model=UserRegisterResponse,
)
async def register(user: UserRegisterRequest):
    controller = UserController()
    return await controller.register(user)


@router.get(
    path="/user",
    status_code=200,
    response_model=User,
)
async def get(token: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    controller = UserController()
    return await controller.get(token)


@router.post(
    path="/login",
    status_code=200,
    response_model=UserLoginResponse,
)
async def login(user: UserLoginRequest):
    controller = UserController()
    return await controller.login(user)
