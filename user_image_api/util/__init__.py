import base64
import binascii

from user_image_api.exception.base import Base64Exception


def is_base_64(image_base64: str):
    try:
        base64.b64decode(image_base64)
    except binascii.Error:
        raise Base64Exception()
