from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from user_image_api.config import DB_SCHEMA
from user_image_api.config.database import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": DB_SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(30), unique=True)
    image = relationship("Image", back_populates="user")

    def __init__(self, name):
        self.user_name = name


class Image(Base):
    __tablename__ = "image"
    __table_args__ = {"schema": DB_SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    thumbnails = Column(String, nullable=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_id = Column(Integer, ForeignKey(f"{DB_SCHEMA}.user.id"))
    user = relationship("User", back_populates="image")

    def __init__(self, image, thumbnails, user_id):
        self.image = image
        self.thumbnails = thumbnails
        self.user_id = user_id
