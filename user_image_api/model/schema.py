from typing import List

from pydantic import BaseModel


class UserInsertInput(BaseModel):
    user_name: str


class UserUpdateInput(BaseModel):
    user_id: int
    user_name: str


class UserOutput(BaseModel):
    user_id: int


# ---image ---
class ImageInsertIn(BaseModel):
    user_id: int
    image_base64: str
    thumbnails: str


class ImageOutput(BaseModel):
    image_id: int


class ImageGetIn(BaseModel):
    user_id: int
    image_id: int


class ImageGetOutput(BaseModel):
    image_base64: str


class ImageThumbUserListOut(BaseModel):
    list_users_image_id: List
    thumb64: str


class UserImageUpdateInput(BaseModel):
    user_id: int
    image_id: int
    image_base64: str


class UserImageUpdateOut(BaseModel):
    user_id: int


class DelUserImageInput(BaseModel):
    user_id: int
    image_id: int


