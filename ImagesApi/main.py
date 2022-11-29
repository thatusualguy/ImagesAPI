import uvicorn
from fastapi import FastAPI, Path

import images
from ImageInfo import ImageInfo
from ImageUpload import ImageUpload

app = FastAPI()


@app.get("/images/{image_name}")
def get_image(image_name: str = Path(regex=images.filename_regex)):
    return images.get_image(image_name)


@app.delete("/images/{image_name}", status_code=200)
def delete_image(image_name: str = Path(regex=images.filename_regex)):
    images.delete_image(image_name)


@app.get("/images", response_model=list[ImageInfo])
def list_images():
    return images.list_images()


@app.post("/images")
def add_image(image: ImageUpload):
    images.add_image(image)


if __name__ == "__main__":
    images.setup(directory="../images/")
    # images.setup(directory=sys.argv[1])
    uvicorn.run(app, host="0.0.0.0", port=8000)
