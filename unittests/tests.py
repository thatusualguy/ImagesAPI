import base64
import json
import unittest

import requests

# from ..ImagesApi.ImageInfo import ImageInfo
# from ..ImagesApi.ImageUpload import ImageUpload

from ImageInfo import ImageInfo
from ImageUpload import ImageUpload

api_url = "http://localhost:8000/images"

image_1 = ImageUpload(name="test_image_1.jpg",
                      data="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")
image_2 = ImageUpload(name="test_image_2.jpg",
                      data="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")

class HappyPathTestCase(unittest.TestCase):
    def test_get_all(self):
        """Only checks the status code."""
        response = requests.get(api_url)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

    def test_add_image(self):
        """Only checks the status code."""
        image = image_1

        response_upload = requests.post(api_url, data=asdata(image))
        self.assertEqual(200, response_upload.status_code, "Should be 200 'OK'")

    def test_add_image_twice(self):
        """Only checks the status code."""
        image = image_1

        for i in range(2):
            response_upload = requests.post(api_url, data=asdata(image))
            self.assertEqual(200, response_upload.status_code, "Should be 200 'OK'")

    def test_get_image(self):
        """Checks the status code and returned file."""
        image = image_1

        requests.post(api_url, data=asdata(image))
        response = requests.get(api_url + '/' + image.name)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        image_base64 = str(base64.b64encode(response.content))[2:-1]
        self.assertEqual(image.data, image_base64, "Images should be equal")

    def test_get_all_some_file(self):
        image = image_1
        requests.post(api_url, data=asdata(image_1))

        response = requests.get(url=api_url)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        contains = contains_image(response, image_1)

        self.assertTrue(contains, "Returned list should contain recently added image.")

    def test_get_all_contains_info(self):
        image = image_1

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.get(url=api_url)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        contains = contains_image(response, image)
        self.assertTrue(contains, "Returned list should contain recently added image.")

        values: list[ImageInfo] = response.json()
        for v in values:
            if v["name"] == image.name:
                v = ImageInfo(**v)
                self.assertIsNotNone(v.name)
                self.assertIsNotNone(v.size)
                self.assertIsNotNone(v.last_modified)

    def test_delete_image(self):
        image = image_1

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.delete(api_url + '/' + image.name)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.get(api_url + '/' + image.name)
        self.assertEqual(404, response.status_code, "Should be 404 'Not Found'")


class ErrorsTestCase(unittest.TestCase):
    def test_delete_twice(self):
        image = image_1

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.delete(api_url + '/' + image.name)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.delete(api_url + '/' + image.name)
        self.assertEqual(404, response.status_code, "Should be 404 'Not Found'")

    def test_get_after_delete(self):
        image = image_1

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.delete(api_url + '/' + image.name)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.get(api_url + '/' + image.name)
        self.assertEqual(404, response.status_code, "Should be 404 'Not Found'")

    def test_list_after_delete(self):
        image = image_1

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.delete(api_url + '/' + image.name)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        response = requests.get(api_url)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        not_contains = not contains_image(response, image)
        self.assertTrue(not_contains, "Should not contain recently deleted image.")

    def test_add_error_image(self):
        image = ImageUpload(name="test_error.jpg", data="error")

        # delete if exists with the same name
        requests.delete(api_url + '/' + image.name)

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(422, response.status_code, "Should be 422 'Unprocessable Entity'")

        response = requests.get(api_url)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        not_contains = not contains_image(response, image)
        self.assertTrue(not_contains, "Should not contain bad image.")

        response = requests.get(api_url + '/' + image.name)
        self.assertEqual(404, response.status_code, "Should be 404 'Not Found'")


class BadFilenamesTestCase(unittest.TestCase):

    def test_bad_name_add(self):
        image = image_1
        image.name = "bad"

        response = requests.post(api_url, data=asdata(image))
        self.assertEqual(422, response.status_code, "Should be 422 'Unprocessable Entity'")

        response = requests.get(api_url)
        self.assertEqual(200, response.status_code, "Should be 200 'OK'")

        not_contains = not contains_image(response, image)
        self.assertTrue(not_contains, "Should not contain bad image.")

        response = requests.get(api_url + '/' + image.name)
        self.assertEqual(422, response.status_code, "Should be 422 'Unprocessable Entity'")

    def test_bad_name_get(self):
        image = image_1
        image.name = "bad"
        response = requests.get(api_url + '/' + image.name)
        self.assertEqual(422, response.status_code, "Should be 422 'Unprocessable Entity'")

    def test_bad_name_delete(self):
        image = image_1
        image.name = "bad"
        response = requests.delete(api_url + '/' + image.name)
        self.assertEqual(422, response.status_code, "Should be 422 'Unprocessable Entity'")

    def test_malicios_name_delete(self):
        image = image_1
        image.name = "../images"
        response = requests.delete(api_url + '/' + image.name)
        self.assertNotEqual(200, response.status_code, "Should be some kind of error")
        self.assertEqual(4, response.status_code // 100, "Should be client error")


def asdata(image: ImageUpload) -> str:
    return json.dumps({"name": image.name, "data": image.data})


def contains_image(response, image):
    body: list[ImageInfo] = response.json()
    for i in body:
        if i["name"] == image.name:
            return True
    return False


if __name__ == '__main__':
    unittest.main()
