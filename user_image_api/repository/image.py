from user_image_api.model.database import Image
from user_image_api.repository import RepositoryBase


class ImageRepository(RepositoryBase):

    def find_image_by_id_and_user(self, user_id, image_id):
        return self.session.query(Image).filter(Image.user_id == user_id, Image.id == image_id).first()

