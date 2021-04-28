
from pydantic import BaseModel


class UserInsertInput(BaseModel):
    user_name: str


class UserUpdateInput(BaseModel):
    user_id: int
    user_name: str


class UserOutput(BaseModel):
    user_id: int


# ---image ---
class ImageInsertInput(BaseModel):
    user_id: int
    image_base64: str


class ImageOutput(BaseModel):
    image_id: int


# class ImageGetIn(BaseModel):
#     user_id: int
#     image_id: int


class ImageGetOutput(BaseModel):
    image_base64: str


class UserImageUpdateInput(BaseModel):
    user_id: int
    image_id: int
    image_base64: str


class UserImageUpdateOut(BaseModel):
    user_id: int


class DelUserImageInput(BaseModel):
    user_id: int
    image_id: int


class ThumbUserListOutput(BaseModel):
    user_id: int
    thumbnails: list
