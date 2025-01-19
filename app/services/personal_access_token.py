from prisma.models import personal_access_tokens
from app.repositories.personal_access_token import PersonalAccessTokenRepository
from app.models.user import User
from app.models.personal_access_token import PersonalAccessToken
from config.log import Log

from dotenv import load_dotenv
from fastapi import HTTPException
import os
import datetime
import jwt
import sys

load_dotenv(override=True)

logger = Log().get_logger(__name__)


class PersonalAccessTokenService:
    def __init__(self):
        self.__personal_access_token_repository = PersonalAccessTokenRepository()
        self.__secret_key = os.getenv("APP_SECRET_KEY", "SECRET")
        self.__algorithm = os.getenv("APP_ALGORITHM", "ALGORITHM")
        self.__expires = os.getenv("APP_ACCESS_TOKEN_EXPIRES_HOURS", 24)

    async def __generate_token(self, user: User) -> str:
        logger.info(f"generate_token: {user}")

        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
            hours=int(self.__expires)
        )

        return jwt.encode(
            payload={"id": user.id, "username": user.username, "exp": expiration},
            key=self.__secret_key,
            algorithm=self.__algorithm,
        )

    async def create(self, user: User) -> PersonalAccessToken:
        logger.info(f"create: {user}")

        token = await self.__generate_token(user)

        personal_access_token = await self.__personal_access_token_repository.create(
            user.id, token
        )

        return PersonalAccessToken(
            id=personal_access_token.id,
            user_id=personal_access_token.user_id,
            token=personal_access_token.token,
            last_used_at=personal_access_token.last_used_at,
            created_at=personal_access_token.created_at,
            updated_at=personal_access_token.updated_at,
        )

    async def get(self, token: str) -> PersonalAccessToken:
        logger.info(f"get: {token}")

        personal_access_token = await self.__personal_access_token_repository.get(token)

        if not personal_access_token:
            logger.info(f"get: personal access token not found: {token}")
            raise HTTPException(status_code=401, detail="Unauthorized")

        decoded = jwt.decode(
            jwt=token,
            key=self.__secret_key,
            algorithms=self.__algorithm,
        )

        logger.info(f"decoded exp: {decoded['exp']}")
        logger.info(
            f"now: {int(datetime.datetime.now(datetime.timezone.utc).timestamp())}"
        )
        logger.info(f"created_at: {int(personal_access_token.created_at.timestamp())}")

        sys.set_int_max_str_digits(65535)
        if (
            decoded["exp"]
            < int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        ) or (
            datetime.datetime.now(datetime.timezone.utc).timestamp()
            - personal_access_token.created_at.timestamp()
            > int(self.__expires) * 3600
        ):
            sys.set_int_max_str_digits(4300)
            logger.info(f"get: token expired: {token}")
            personal_access_token = (
                await self.__personal_access_token_repository.delete(
                    personal_access_token.id
                )
            )
            raise HTTPException(status_code=401, detail="Expired token")

        return PersonalAccessToken(
            id=personal_access_token.id,
            user_id=personal_access_token.user_id,
            token=personal_access_token.token,
            last_used_at=personal_access_token.last_used_at,
            created_at=personal_access_token.created_at,
            updated_at=personal_access_token.updated_at,
        )

    async def last_used_at(self, user_id: int, token: str):
        logger.info(f"last_used_at: {user_id}, {token}")

        return await self.__personal_access_token_repository.last_used_at(
            user_id, token
        )
