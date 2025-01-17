from config.log import Log
from app.services.user import UserService
from app.models.user import User
from app.schemas.requests.user import UserRegisterRequest
from app.schemas.requests.user import UserLoginRequest
from app.schemas.responses.user import UserRegisterResponse
from app.schemas.responses.user import UserLoginResponse

from fastapi import HTTPException

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

        except Exception as e:
            logger.error(f"register: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
