import base64
import binascii
import io

from PIL import Image

from user_image_api.exception.base import Base64Exception


def is_base_64(image_base64: str):
    try:
        base64.b64decode(image_base64)
    except binascii.Error:
        raise Base64Exception()


def get_thumbnails(image_base64: str):
    is_base_64(image_base64)

    size = 100, 100
    buffer = io.BytesIO()
    imgdata = base64.b64decode(image_base64)
    img = Image.open(io.BytesIO(imgdata))
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(buffer, format="PNG")
    thumb = base64.b64encode(buffer.getvalue())

    return str(thumb)[2:-1]
