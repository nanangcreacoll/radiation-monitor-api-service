from app.repositories.personal_access_token import PersonalAccessTokenRepository


class PersonalAccessTokenService:
    def __init__(self):
        self.__personal_access_token_repository = PersonalAccessTokenRepository()
