from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from user_image_api.config import VERSION
from user_image_api.config.database import get_db
from user_image_api.model.schema import (DelUserImageInput, ImageGetOutput,
                                         ImageInsertInput, ImageOutput,
                                         ThumbUserListOutput,
                                         UserImageUpdateInput)
from user_image_api.service import image

router = APIRouter()


@router.post(f'/v{VERSION}/add-user-image', status_code=201, summary="Add User Image", response_model=ImageOutput)
def add_user_image(payload: ImageInsertInput, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    image_id = service.add_image(payload)
    return ImageOutput(image_id=image_id)


@router.get(f'/v{VERSION}/get-user-image/<user_id>/<image_id>', status_code=200, summary="Get User Image",
            response_model=ImageGetOutput)
def get_user_image(user_id, image_id, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    image64 = service.get_image(user_id, image_id)
    return ImageGetOutput(image_base64=image64)


@router.get(f'/v{VERSION}/list-user-images-thumbnails/<user_id>', status_code=200, summary="List User Image Thumbnails",
            response_model=ThumbUserListOutput)
def list_user_images_thumb(user_id, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    return service.get_thumbnails(user_id)


@router.put(f'/v{VERSION}/update-user-image', status_code=200, summary="Update User image")
def update_user_image(payload: UserImageUpdateInput, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    service.update_image(payload)
    return "User Image Updated"


@router.delete(f'/v{VERSION}/delete-user-image', status_code=200, summary="Delete User Image")
def delete_user_image(payload: DelUserImageInput, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    service.delete_image(payload.user_id, payload.image_id)
    return "User Image Deleted"
