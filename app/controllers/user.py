from config.log import Log
from app.services.user import UserService
from app.schemas.responses.user import User
from app.schemas.requests.user import UserRegisterRequest
from app.schemas.requests.user import UserLoginRequest
from app.schemas.responses.user import UserRegisterResponse
from app.schemas.responses.user import UserLoginResponse

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

logger = Log().get_logger(__name__)


class UserController:
    def __init__(self):
        self.__user_service = UserService()

    async def register(self, user: UserRegisterRequest) -> UserRegisterResponse:
        logger.info(f"register: {user}")

        try:
            user_created = await self.__user_service.register(user)

            return UserRegisterResponse(
                id=user_created.id,
                username=user_created.username,
            )

        except HTTPException as e:
            logger.info(f"register: {e}")
            raise e

    async def login(self, user: UserLoginRequest) -> UserLoginResponse:
        logger.info(f"login: {user}")

        try:
            user_logged = await self.__user_service.login(user)

            return UserLoginResponse(
                type="bearer",
                token=user_logged.token,
            )

        except HTTPException as e:
            logger.info(f"login: {e}")
            raise e

    async def get(
        self, token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer)]
    ) -> User:
        logger.info(f"get user: {token}")

        try:
            user = await self.__user_service.get(token.credentials)

            return User(
                id=user.id,
                username=user.username,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )

        except HTTPException as e:
            logger.info(f"get: {e}")
            raise e
