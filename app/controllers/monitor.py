from config.log import Log
from app.services.monitor import MonitorService
from app.schemas.requests.monitor import MonitorRequest
from app.schemas.responses.monitor import MonitorResponse

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

logger = Log().get_logger(__name__)


class MonitorController:
    def __init__(self):
        self.__monitor_service = MonitorService()

    async def create(
        self,
        token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer)],
        monitor: MonitorRequest,
    ) -> MonitorResponse:
        logger.info(f"create: {monitor}")

        try:
            monitor_created = await self.__monitor_service.create(
                token.credentials, monitor
            )

            return MonitorResponse(
                id=monitor_created.id,
                temperature=monitor_created.temperature,
                humidity=monitor_created.humidity,
                dose_rate=monitor_created.dose_rate,
                created_at=monitor_created.created_at,
            )

        except HTTPException as e:
            logger.info(f"create: {e}")
            raise e
