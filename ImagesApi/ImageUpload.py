from pydantic import BaseModel


class ImageUpload(BaseModel):
    name: str
    data: str
