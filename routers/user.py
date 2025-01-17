from app.controllers.user import UserController
from app.schemas.requests.user import UserRegisterRequest

from fastapi import Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()

security = HTTPBearer()


@router.post("/user")
async def register(user: UserRegisterRequest):
    controller = UserController()
    return await controller.register(user)


@router.get("/user")
async def read_users(token: HTTPAuthorizationCredentials = Depends(security)):
    return {
        "token": token.credentials,
        "scheme": token.scheme,
    }
