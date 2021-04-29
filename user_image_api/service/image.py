from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from user_image_api.exception.base import (NoExistException,
                                           SQLAlchemyException, TypeException,
                                           UniqueException)
from user_image_api.model.database import Image
from user_image_api.model.schema import (ImageInsertInput, ThumbUserListOutput,
                                         UserImageUpdateInput)
from user_image_api.repository.image import ImageRepository
from user_image_api.util import get_thumbnails, is_base_64


class ImageService:

    def __init__(self, session: Session):
        self.image_repo = ImageRepository(session)

    def add_image(self, payload: ImageInsertInput):
        is_base_64(payload.image_base64)
        try:
            image_model = Image(payload.image_base64,
                                get_thumbnails(payload.image_base64),
                                payload.user_id
                                )
            image = self.image_repo.save(image_model)
            return image.id
        except IntegrityError:
            raise NoExistException()
        except SQLAlchemyError:
            raise SQLAlchemyException()

    def get_image(self, user_id, image_id):
        try:
            model_image = self.image_repo.find_image_by_id_and_user(
                user_id,
                image_id
            )
            if model_image:
                return model_image.image
            return "Empty Value, check user_id or image_id"
        except IntegrityError:
            raise NoExistException()
        except SQLAlchemyError:
            raise TypeException()

    def update_image(self, payload: UserImageUpdateInput):
        is_base_64(payload.image_base64)

        try:
            self.image_repo.update_user_image_by_user_and_image_id(
                payload.user_id,
                payload.image_id,
                {"image": payload.image_base64}
            )
        except IntegrityError:
            raise UniqueException()
        except SQLAlchemyError:
            raise SQLAlchemyException()

    def delete_image(self, user_id, image_id):
        try:
            self.image_repo.del_user_image_by_user_id_and_image_id(
                                                                    user_id,
                                                                    image_id)
        except SQLAlchemyError:
            raise SQLAlchemyException()

    def get_thumbnails(self, user_id):
        try:
            thumbnails = self.image_repo.find_thumb_by_user_id(user_id)
            return ThumbUserListOutput(user_id=user_id, thumbnails=thumbnails)
        except SQLAlchemyError:
            raise SQLAlchemyException()
