from config.prisma import prisma


class UserRepository:
    def __init__(self):
        self.__prisma = prisma

    async def create(self, username: str, password: str):
        return await self.__prisma.users.create(
            data={"username": username, "password": password}
        )

    async def get_by_id(self, user_id: int):
        return await self.__prisma.users.find_unique(where={"id": user_id})

    async def get_by_username(self, username: str):
        return await self.__prisma.users.find_first(where={"username": username})
