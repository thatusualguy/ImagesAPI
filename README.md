# ImagesAPI

## Setup
```
git clone https://github.com/thatusualguy/ImagesAPI
cd ImagesAPI
docker volume create ImagesAPI
docker compose up
```
After the container is launched, you can visit [localhost:8000/images](http://localhost:8000/images) to access API.
## Docs
After launching container, API docs are located at
- [localhost:8000/docs](http://localhost:8000/docs) with Swagger UI
- [localhost:8000/redoc](http://localhost:8000/redoc) with ReDoc
## Storage
All images saved by API are stored in `ImagesAPI` Docker volume.
## Prerequsites
- Git
- Docker
