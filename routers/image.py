import io
import os
import uuid

from PIL import Image
from fastapi import APIRouter, UploadFile, File
from starlette.responses import FileResponse

from properties import IMAGE_DIR

router = APIRouter(
    prefix="/image",
    tags=["image"]
)


@router.get("/{image_name}")
async def get_image(image_name: str):
    return FileResponse(''.join([IMAGE_DIR, image_name]), media_type="image/webp")


@router.post("")
async def post_image(image: UploadFile = File(...)):
    image_name = uuid.uuid4().hex
    image_location = os.path.join(IMAGE_DIR, image_name)

    # save to .webp
    image_io = await image.read()
    im = Image.open(io.BytesIO(image_io))
    im.save(image_location, "webp")

    return image_name
