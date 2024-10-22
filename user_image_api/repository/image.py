from user_image_api.model.database import Image
from user_image_api.repository import RepositoryBase


class ImageRepository(RepositoryBase):

    def find_thumb_by_user_id(self, user_id):
        return self.session.query(Image.thumbnails).filter(
            Image.user_id == user_id).all()

    def find_image_by_id_and_user(self, user_id, image_id):
        return self.session.query(Image).filter(Image.user_id == user_id,
                                                Image.id == image_id).first()

    def update_user_image_by_user_and_image_id(self, user_id: int,
                                               image_id: int,
                                               values: dict):
        self.session.query(Image).filter(Image.user_id == user_id,
                                         Image.id == image_id).update(values)
        self.session.commit()

    def del_user_image_by_user_id_and_image_id(self, user_id, image_id):
        self.session.query(Image).filter(Image.user_id == user_id,
                                         Image.id == image_id).delete()
        self.session.commit()
