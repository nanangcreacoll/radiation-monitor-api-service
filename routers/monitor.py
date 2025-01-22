from app.controllers.monitor import MonitorController
from app.schemas.requests.monitor import MonitorRequest
from app.schemas.responses.monitor import MonitorResponse

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

router = APIRouter()

security = HTTPBearer()


@router.post(
    path="/monitor",
    status_code=201,
    response_model=MonitorResponse,
)
async def create(
    token: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    monitor: MonitorRequest,
):
    controller = MonitorController()
    return await controller.create(token, monitor)
