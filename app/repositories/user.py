from app.schemas.requests.user import UserRegister
from app import prisma


class User:
    def __init__(self):
        self.__prisma = prisma

    async def create_user(self, user: UserRegister):
        return await self.__prisma.users.create(
            data={"username": user.username, "password": user.password}
        )

    async def get_user_by_id(self, user_id: int):
        return await self.__prisma.users.find_first(where={"id": user_id})
