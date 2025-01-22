from app.repositories.monitor import MonitorRepository
from app.models.user import User
from app.models.monitor import Monitor
from app.schemas.requests.monitor import MonitorRequest
from app.services.user import UserService
from config.log import Log

logger = Log().get_logger(__name__)


class MonitorService:
    def __init__(self):
        self.__monitor_repository = MonitorRepository()
        self.__user_service = UserService()

    async def create(self, token: str, monitor: MonitorRequest) -> Monitor:
        logger.info(f"create: {monitor}")

        user: User = await self.__user_service.get(token)

        monitor_created = await self.__monitor_repository.create(user, monitor)

        return Monitor(
            id=monitor_created.id,
            user_id=monitor_created.user_id,
            temperature=monitor_created.temperature,
            humidity=monitor_created.humidity,
            dose_rate=monitor_created.dose_rate,
            created_at=monitor_created.created_at,
        )
