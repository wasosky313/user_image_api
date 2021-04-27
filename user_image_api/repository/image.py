
from user_image_api import model
from user_image_api.config.database import Base
from user_image_api.repository import RepositoryBase


class ImageRepository(RepositoryBase):

    def list(self, model: Base, image_id: int):
        return self.session.query(model.Image).filter(model.Image.id == image_id).first()

