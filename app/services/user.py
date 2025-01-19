from app.models.user import User
from app.models.personal_access_token import PersonalAccessToken
from app.services.personal_access_token import PersonalAccessTokenService
from app.repositories.user import UserRepository
from app.schemas.requests.user import UserRegisterRequest, UserLoginRequest
from config.log import Log

from passlib.context import CryptContext
from fastapi import HTTPException

logger = Log().get_logger(__name__)


class UserService:
    def __init__(self):
        self.__user_repository = UserRepository()
        self.__personal_access_token_service = PersonalAccessTokenService()
        self.__hash = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register(self, user_register: UserRegisterRequest) -> User:
        logger.info(f"register: {user_register}")

        user_by_username = await self.__user_repository.get_by_username(
            user_register.username
        )

        if user_by_username:
            logger.info(f"register: user already exists: {user_by_username}")
            raise HTTPException(status_code=400, detail="User already exists")

        hashed_password = self.__hash.hash(user_register.password)

        user_created = await self.__user_repository.create(
            user_register.username, hashed_password
        )

        return User(
            id=user_created.id,
            username=user_created.username,
            password=user_created.password,
            created_at=user_created.created_at,
            updated_at=user_created.updated_at,
        )

    async def login(self, user_login: UserLoginRequest) -> PersonalAccessToken:
        logger.info(f"login: {user_login}")

        user_by_username = await self.__user_repository.get_by_username(
            user_login.username
        )

        if not user_by_username:
            logger.info(f"login: user not found: {user_login}")
            raise HTTPException(status_code=400, detail="Username or password invalid")

        if not self.__hash.verify(user_login.password, user_by_username.password):
            logger.info(f"login: invalid password: {user_login}")
            raise HTTPException(status_code=400, detail="Username or password invalid")

        user = User(
            id=user_by_username.id,
            username=user_by_username.username,
            password=user_by_username.password,
            created_at=user_by_username.created_at,
            updated_at=user_by_username.updated_at,
        )

        personal_access_token = await self.__personal_access_token_service.create(user)

        return PersonalAccessToken(
            id=personal_access_token.id,
            user_id=personal_access_token.user_id,
            token=personal_access_token.token,
            last_used_at=personal_access_token.last_used_at,
            created_at=personal_access_token.created_at,
            updated_at=personal_access_token.updated_at,
        )

    async def get(self, token: str) -> User:
        logger.info(f"get: {token}")

        personal_access_token = await self.__personal_access_token_service.get(token)

        user = await self.__user_repository.get_by_id(personal_access_token.user_id)

        personal_access_token = await self.__personal_access_token_service.last_used_at(
            user.id, token
        )

        return User(
            id=user.id,
            username=user.username,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
