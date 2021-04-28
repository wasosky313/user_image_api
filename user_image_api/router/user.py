from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from user_image_api.config import VERSION
from user_image_api.config.database import get_db
from user_image_api.model.schema import (UserInsertInput, UserOutput,
                                         UserUpdateInput)
from user_image_api.service import user

router = APIRouter()


@router.post(f'/v{VERSION}/add-user', status_code=201, summary="Add User", response_model=UserOutput)
def add_user(payload: UserInsertInput, session: Session = Depends(get_db)):
    service = user.UserService(session)
    usr_id = service.add(payload)
    return UserOutput(user_id=usr_id)


@router.put(f'/v{VERSION}/update-user', status_code=200, summary="Update User", response_model=UserOutput)
def update_user(payload: UserUpdateInput, session: Session = Depends(get_db)):
    service = user.UserService(session)
    service.update(payload)
    return UserOutput(user_id=payload.user_id)
