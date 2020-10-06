import unittest
from app import app
import json
import requests


class FlaskClientTestCase(unittest.TestCase):

        def test_index(self):
                tester = app.test_client(self)
                response = tester.get("/")
                statuscode = response.status_code
                self.assertEqual(statuscode, 200)

        def test_somos_kudasai(self):
            tester = app.test_client(self)
            response = tester.get('/news/gHw5fnQBlUGqDnjfb4X-')
            json_data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            assert 'author' in json_data
            assert 'title' in json_data
            assert 'text' in json_data
            assert 'created_at' in json_data
            assert 'url' in json_data
            #assert 'tags' in json_data['email']['attributes']
        
        def test_teheran_news(self):
            tester = app.test_client(self)
            response = tester.get('/news/eT_gb3QBsGJNd5nCNxyN')
            json_data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            assert 'title' in json_data
            assert 'topic' in json_data
            assert 'text' in json_data
            assert 'created_at' in json_data
            assert 'url' in json_data

        def test_post(self):
            article = {
                "title": "The test title",
                "text": "The test body",
                "created_at": "2020-09-15T11:53:00"
            }
            tester = app.test_client(self)
            response = tester.post("/create-teheran-news-article".format(), json=article)
            json_data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            assert 'title' in json_data
            assert 'text' in json_data
            assert 'created_at' in json_data

if __name__ == "__main__":
    unittest.main()
