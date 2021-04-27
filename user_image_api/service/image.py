from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from user_image_api.exception.base import UniqueException
from user_image_api.model.database import Image
from user_image_api.model.schema import ImageInsertIn, ImageGetIn
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

    def get(self, payload: ImageGetIn):
        pass


