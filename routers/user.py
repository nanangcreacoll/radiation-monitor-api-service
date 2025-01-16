from fastapi import Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()

security = HTTPBearer()


@router.get("/user")
async def read_users(token: HTTPAuthorizationCredentials = Depends(security)):
    return {
        "token": token.credentials,
        "scheme": token.scheme,
    }
