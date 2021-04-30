from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from user_image_api.config import VERSION
from user_image_api.config.database import get_db
from user_image_api.model.schema import (UserInsertInput, UserOutput,
                                         UserUpdateInput)
from user_image_api.service import user
from user_image_api.task.rabbitmq import publish_message

router = APIRouter()


@router.post(f'/v{VERSION}/add-user',
             status_code=201,
             summary="Add User",
             response_model=UserOutput)
def add_user(payload: UserInsertInput,
             background_tasks: BackgroundTasks,
             session: Session = Depends(get_db)):
    service = user.UserService(session)
    user_model = service.add(payload)
    background_tasks.add_task(publish_message, user_model.id, user_model.user_name, 0, "/add-user")
    return UserOutput(user_id=user_model.id)


@router.put(f'/v{VERSION}/update-user',
            status_code=200,
            summary="Update User",
            response_model=UserOutput)
def update_user(payload: UserUpdateInput, background_tasks: BackgroundTasks, session: Session = Depends(get_db)):
    service = user.UserService(session)
    service.update(payload)
    background_tasks.add_task(publish_message, payload.user_id, payload.user_name, 0, "/update-user")
    return UserOutput(user_id=payload.user_id)
