from config.prisma import prisma
from app.models.user import User
from app.schemas.requests.monitor import MonitorRequest
import datetime


class MonitorRepository:
    def __init__(self):
        self.__prisma = prisma

    async def create(self, user: User, monitor: MonitorRequest):
        return await self.__prisma.monitor.create(
            data={
                "user": {"connect": {"id": user.id}},
                "temperature": monitor.temperature,
                "humidity": monitor.humidity,
                "dose_rate": monitor.dose_rate,
                "created_at": datetime.datetime.now(datetime.timezone.utc),
            }
        )
