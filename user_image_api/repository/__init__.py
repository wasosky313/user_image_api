
from sqlalchemy.orm import Session

from user_image_api.config.database import Base


class RepositoryBase:

    def __init__(self, session: Session):
        self.session = session

    def save(self, model: Base):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def update(self, model: Base, model_id: int, values: dict):
        self.session.query(model).filter(model.id == model_id).update(values)
        self.session.commit()
