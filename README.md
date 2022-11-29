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
## Tests
Can only be launched from PyCharm IDE. Otherwise linkning to data classes fails.
- Install requrments.txt from `unittests` folder
- From IDE launch HappyPathTestCase, ErrorsTestCase, BadFilenamesTestCase 

Another way is to copy files `ImageUpload.py` and `ImageInfo.py` to `unittests` directory and then launch tests.
```
>>> python -m unittest tests.HappyPathTestCase tests.ErrorsTestCase tests.BadFilenamesTestCase --verbose
test_get_all_some_file (tests.HappyPathTestCase) ... ok
test_get_image (tests.HappyPathTestCase)
Checks the status code and returned file. ... ok
test_add_error_image (tests.ErrorsTestCase) ... ok
test_delete_twice (tests.ErrorsTestCase) ... ok
test_get_after_delete (tests.ErrorsTestCase) ... ok
test_list_after_delete (tests.ErrorsTestCase) ... ok
test_bad_name_add (tests.BadFilenamesTestCase) ... ok
test_bad_name_delete (tests.BadFilenamesTestCase) ... ok
test_bad_name_get (tests.BadFilenamesTestCase) ... ok
test_malicios_name_delete (tests.BadFilenamesTestCase) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.177s

OK
```

## Prerequsites
- Git
- Docker
