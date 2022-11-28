from pathlib import Path
from re import match
from base64 import b64decode
import os
from datetime import datetime, timezone

from fastapi import HTTPException
from fastapi.responses import FileResponse

from ImageInfo import ImageInfo
from ImageUpload import ImageUpload

image_dir = "./images/"
filename_regex = r"^\w+.jpg$"


def setup(directory: str) -> None:
    """Takes directory used to store images."""
    global image_dir
    image_dir = directory

    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)


def list_images() -> list[ImageInfo]:
    """Visits directory and returns a list of file info."""
    if not os.path.isdir(image_dir):
        return []

    images: list[ImageInfo] = []
    for image_name in os.listdir(image_dir):
        image_path: str = build_path(image_name)
        if not os.path.isfile(image_path):
            continue

        name: str = os.path.basename(image_path)
        size: int = os.path.getsize(image_path)
        last_modified: datetime = datetime.fromtimestamp(round(os.path.getmtime(image_path))).astimezone(timezone.utc)
        info: ImageInfo = ImageInfo(name=name, size=size, last_modified=last_modified)
        images.append(info)

    return images


def get_image(image_name: str) -> FileResponse:
    """Takes image path and returns the file."""
    image_path: str = build_path(image_name)
    if not os.path.isfile(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)


def add_image(image: ImageUpload) -> None:
    """Takes image name and data, saves it as file."""
    if not os.path.isdir(image_dir):
        raise HTTPException(status_code=500, detail="No image directory found")

    if not match(r"^\w+.jpg$", image.name):
        raise HTTPException(status_code=400, detail="Invalid filename")

    image_path: str = build_path(image.name)
    # try:
    with open(image_path, "wb") as f:
        f.write(b64decode(image.data))
    # except:
    #     raise HTTPException(status_code=500, detail="Unable to save image")


def delete_image(image_name: str) -> None:
    """Takes image name and deletes the file from filesystem."""
    image_path: str = build_path(image_name)
    if not os.path.isfile(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    os.remove(image_path)


def build_path(image_name: str) -> str:
    """Takes image name and returns path to it."""
    return os.path.join(image_dir, image_name)
