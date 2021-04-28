from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user_image_api.config import VERSION

from user_image_api.config.database import get_db
from user_image_api.model.schema import ImageOutput, ImageInsertIn, ImageGetOutput, ImageThumbUserListOut, \
    UserImageUpdateInput, UserImageUpdateOut, DelUserImageInput
from user_image_api.service import image

router = APIRouter()


@router.post(f'/v{VERSION}/add-user-image', status_code=201, summary="Add User Image", response_model=ImageOutput)
def add(payload: ImageInsertIn, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    image_id = service.add(payload)
    return ImageOutput(image_id=image_id)


@router.get(f'/v{VERSION}/get-user-image/<user_id>/<image_id>', status_code=200, summary="Get User Image",
            response_model=ImageGetOutput)
def get_user_image(user_id, image_id, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    image64 = service.get(user_id, image_id)
    return ImageGetOutput(image_base64=image64)


# Unfinished, see later
@router.get(f'/v{VERSION}/list-user-images-thumb/<user_id>', status_code=200, summary="list User Images Thumb",
            response_model=ImageThumbUserListOut)
def list_user_images_thumb(user_id, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    thumb_list = service.get_thumb(user_id)
    return ImageThumbUserListOut(list_users_image_id=thumb_list)


@router.put(f'/v{VERSION}/update-user-image', status_code=200, summary="Update User image")
def update_user_image(payload: UserImageUpdateInput, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    service.update(payload)
    return "User Image Updated"


@router.delete(f'/v{VERSION}/delete-user-image', status_code=200, summary="Delete User Image")
def delete_user_image(payload: DelUserImageInput, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    service.delete(payload.user_id, payload.image_id)
    return "User Image Deleted"