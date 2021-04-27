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
