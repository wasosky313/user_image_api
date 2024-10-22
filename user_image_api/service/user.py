from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from user_image_api.exception.base import (NoExistException,
                                           SQLAlchemyException,
                                           UniqueException)
from user_image_api.model.database import User
from user_image_api.model.schema import UserInsertInput, UserUpdateInput
from user_image_api.repository.user import UserRepository


class UserService:

    def __init__(self, session: Session):
        self.user_repo = UserRepository(session)

    def add(self, payload: UserInsertInput) -> User:
        try:
            user_model = User(payload.user_name)
            user = self.user_repo.save(user_model)
            return user
        except SQLAlchemyError:
            raise UniqueException()
        except IntegrityError:
            raise NoExistException()

    def update(self, payload: UserUpdateInput):
        try:
            self.user_repo.update(
                User,
                payload.user_id,
                {"user_name": payload.user_name}
            )
        except IntegrityError:
            raise UniqueException()
        except SQLAlchemyError:
            raise SQLAlchemyException()
