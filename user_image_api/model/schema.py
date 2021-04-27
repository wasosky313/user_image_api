from pydantic import BaseModel


class UserInsertInput(BaseModel):
    user_name: str


class UserUpdateInput(BaseModel):
    user_id: int
    user_name: str


class UserOutput(BaseModel):
    user_id: int