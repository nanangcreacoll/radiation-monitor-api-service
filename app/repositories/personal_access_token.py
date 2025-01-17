from config.prisma import prisma
from datetime import datetime


class PersonalAccessTokenRepository:
    def __init__(self):
        self.__prisma = prisma

    async def create(self, user_id: int, token: str):
        return await self.__prisma.personal_access_tokens.create(
            data={"user_id": user_id, "token": token}
        )

    async def get(self, user_id: int, token: str):
        return await self.__prisma.personal_access_tokens.find_first(
            where={"user_id": user_id, "token": token}
        )

    async def update_last_used(self, user_id: int, token: str):
        return await self.__prisma.personal_access_tokens.update(
            where={"user_id": user_id, "token": token},
            data={"last_used_at": datetime.now()},
        )
