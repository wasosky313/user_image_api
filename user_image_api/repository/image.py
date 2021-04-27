from sqlalchemy.orm import Session
from user_image_api.model import database
from user_image_api.config.database import Base
from user_image_api.repository import RepositoryBase


class ImageRepository(RepositoryBase):

    # def list(self, model: Base, image_id: int):
    #     return self.session.query(model.Image).filter(model.Image.id == image_id).first()

    def get_image(self, model: Base, image_id: int):
        return self.session.query(model.Image).filter(model.Image.id == image_id).first()

