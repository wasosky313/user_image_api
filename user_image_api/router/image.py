from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user_image_api.config import VERSION

from user_image_api.config.database import get_db
from user_image_api.model.schema import ImageOutput, ImageInsertIn, ImageGetOutput, ImageGetIn
from user_image_api.service import image

router = APIRouter()


@router.post(f'/v{VERSION}/add-user-image', status_code=201, summary="Add User Image", response_model=ImageOutput)
def add(payload: ImageInsertIn, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    image_id = service.add(payload)
    return ImageOutput(image_id=image_id)


@router.get(f'/v{VERSION}/get-user-image', status_code=200, summary="Get User Image", response_model=ImageGetOutput)
# def get(payload: ImageGetIn, session: Session = Depends(get_db)):
#     # service = image.ImageService(session)
#     # image64 = service.get(payload)
#     return ImageGetOutput(image_base64="image64 test")
def test():
    return ImageGetOutput(image_base64="Testando")
