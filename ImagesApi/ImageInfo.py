from datetime import datetime

from pydantic import BaseModel


class ImageInfo(BaseModel):
    """
    The ImageInfo object contains info about image


    Attributes:
        name (str): the name of image,
        size (int): size of image file in bytes,
        last_modified (datetime): the last modified date of the file (UTC timezone)
    """
    name: str
    size: int
    last_modified: datetime
