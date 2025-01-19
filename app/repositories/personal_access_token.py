from config.prisma import prisma
import datetime


class PersonalAccessTokenRepository:
    def __init__(self):
        self.__prisma = prisma

    async def create(self, user_id: int, token: str):
        return await self.__prisma.personal_access_tokens.create(
            data={"user_id": user_id, "token": token}
        )

    async def delete(self, id: int):
        return await self.__prisma.personal_access_tokens.delete(where={"id": id})

    async def get(self, token: str):
        return await self.__prisma.personal_access_tokens.find_unique(
            where={"token": token}
        )

    async def last_used_at(self, user_id: int, token: str):
        return await self.__prisma.personal_access_tokens.update(
            where={"user_id": user_id, "token": token},
            data={"last_used_at": datetime.datetime.now(datetime.timezone.utc)},
        )
