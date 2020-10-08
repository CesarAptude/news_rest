import unittest
from app import app
import json
import requests


class FlaskClientTestCase(unittest.TestCase):

    def setUp(self):
        return app.test_client()

    def test_index(self):
        response = self.setUp().get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_somos_kudasai(self):
        response = self.setUp().get('/news/xXxJfnQBlUGqDnjfBZrT')
        json_data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('author', json_data)
        self.assertIn('title', json_data)
        self.assertIn('text', json_data)
        self.assertIn('created_at', json_data)
        self.assertIn('url', json_data)
    
    def test_teheran_news(self):
        response = self.setUp().get('/news/eT_gb3QBsGJNd5nCNxyN')
        json_data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('title', json_data)
        self.assertIn('topic', json_data)
        self.assertIn('text', json_data)
        self.assertIn('created_at', json_data)
        self.assertIn('url', json_data)

    def test_post(self):
        article = {
            "title": "The test title",
            "text": "The test body",
            "created_at": "2020-09-15T11:53:00"
        }
        response = self.setUp().post("/create-teheran-news-article".format(), json=article)
        json_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', json_data)
        self.assertIn('text', json_data)
        self.assertIn('created_at', json_data)
    
    def test_put(self):
        article = {
            "title": "The test title",
            "text": "The test body",
            "created_at": "2020-09-15T11:53:00"
        }
        response = self.setUp().put("/news/l3xofnQBlUGqDnjf5MKU".format(), json=article)
        json_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', json_data)
        self.assertIn('text', json_data)
        self.assertIn('created_at', json_data)

    def test_delete(self):
        response = self.setUp().delete("/news/TXxsfnQBlUGqDnjfTcWd")
        json_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', json_data)

    def test_pagination(self):
        article = {
            "keyword": "test"
        }
        response = self.setUp().post('/news-list?page=2&size=10'.format(), json=article)
        json_data = json.loads(response.data)
        size = 10

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_data), size)
        for news in json_data:
            self.assertIn('_id', news)
            self.assertIn('title', news['_source'])
            self.assertIn('text', news['_source'])
            self.assertIn('created_at', news['_source'])


if __name__ == "__main__":
    unittest.main()
