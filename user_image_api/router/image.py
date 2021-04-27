from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user_image_api.config import VERSION

from user_image_api.config.database import get_db
from user_image_api.model.schema import ImageOutput, ImageInsertIn
from user_image_api.service import image

router = APIRouter()


@router.post(f'/v{VERSION}/add-user-image', status_code=201, summary="Add User Image",  response_model=ImageOutput)
def add(payload: ImageInsertIn, session: Session = Depends(get_db)):
    service = image.ImageService(session)
    image_id = service.add(payload)
    return ImageOutput(image_id=image_id)

