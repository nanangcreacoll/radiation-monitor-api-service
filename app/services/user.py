from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.requests.user import UserRegisterRequest
from config.log import Log

from passlib.context import CryptContext
from fastapi import HTTPException

logger = Log().get_logger(__name__)


class UserService:
    def __init__(self):
        self.__user_repository = UserRepository()
        self.__hash = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register(self, user: UserRegisterRequest) -> User:
        logger.info(f"register: {user}")

        user_by_username = await self.__user_repository.get_by_username(user.username)

        if user_by_username:
            logger.info(f"register: user already exists: {user_by_username}")
            raise HTTPException(status_code=400, detail="User already exists")

        hashed_password = self.__hash.hash(user.password)

        user_created = await self.__user_repository.create(
            user.username, hashed_password
        )

        return User(
            id=user_created.id,
            username=user_created.username,
            password=user_created.password,
            created_at=user_created.created_at,
            updated_at=user_created.updated_at,
        )
