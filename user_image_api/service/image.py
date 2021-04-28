from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from user_image_api.exception.base import UniqueException, SQLAlchemyException
from user_image_api.model.database import Image
from user_image_api.model.schema import ImageInsertIn, UserImageUpdateInput
from user_image_api.repository.image import ImageRepository


class ImageService:

    def __init__(self, session: Session):
        self.image_repo = ImageRepository(session)

    def add(self, payload: ImageInsertIn):
        try:
            image_model = Image(payload.image_base64, payload.thumbnails, payload.user_id)
            image = self.image_repo.save(image_model)
            return image.id
        except IntegrityError:
            raise UniqueException()

    def get(self, user_id, image_id):
        try:
            model_image = self.image_repo.find_image_by_id_and_user(user_id, image_id)
            if model_image:
                return model_image.image
            return "Empty Value, check user_id or image_id"
        except IntegrityError:
            raise UniqueException()
        except SQLAlchemyError as err:
            print(err)
            raise SQLAlchemyException()

    def get_thumb(self, user_id):
        model_image = self.image_repo.find_thumb_by_user_id(user_id)
        return model_image

    def update(self, payload: UserImageUpdateInput):
        try:
            self.image_repo.update_user_image_by_user_and_image_id(
                payload.user_id,
                payload.image_id,
                {"image": payload.image_base64}
            )
        except IntegrityError:
            raise UniqueException()

    def delete(self, user_id, image_id):
        self.image_repo.del_user_image_by_ids(user_id, image_id)
