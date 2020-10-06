from flask_restful import Resource
from flask import Flask, request, jsonify
from elasticsearch_dsl.connections import connections
from elasticsearch.exceptions import NotFoundError, RequestError

from utils.utils import Pagination
from models.somos_kudasai import Somos_kudasai
from models.teheran_news import Teheran_news


connections.create_connection(hosts=['localhost'])

pagination = Pagination()
Teheran_news.init()
Somos_kudasai.init()

class Base(Resource):
    def get(self):
        return "Hello"

class News(Resource):
    def get(self, news_id: str):
        try:
            article = Somos_kudasai.get(id = news_id)
        except NotFoundError:
            article = Teheran_news.get(id = news_id)
        except NotFoundError:
            return({'Message': 'Article not found'})
        #print(article.to_dict(['meta'])['_index'])
        return jsonify(article.to_dict())

    def delete(self, news_id: str):
        try:
            article = Somos_kudasai.get(id = news_id)
        except NotFoundError:
            article = Teheran_news.get(id = news_id)
        except NotFoundError:
            return({'Message': 'Article not found'})
        article.delete()
        return {"message":"Article deleted"}

    def put(self, news_id: str):
        try:
            article = Somos_kudasai.get(id = news_id)
        except NotFoundError:
            article = Teheran_news.get(id = news_id)
        except NotFoundError:
            return({'Message': 'Article not found'})
        article.update(published=True, **request.json)
        return jsonify(article.to_dict())


class Create_sk_article(Resource):
    def post(self):
        article = Somos_kudasai(**request.json, published=True)
        article.save()
        print(article.to_dict(['meta']))
        return jsonify(article.to_dict())


class Create_tn_article(Resource):
    def post(self):
        article = Teheran_news(**request.json, published=True)
        article.save()
        print(article.to_dict(['meta']))
        return jsonify(article.to_dict())


class News_list(Resource):
    def post(self):
        try:
            keyword = request.json['keyword']
            return pagination.search(keyword, **request.args)
        except RequestError:
            return {"message": "One of the field of querystring is wrong"}, 400