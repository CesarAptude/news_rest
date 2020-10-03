from flask_restful import Resource
from flask import jsonify
from elasticsearch import Elasticsearch

es = Elasticsearch()


class Pagination():
    def search(self, keyword, page=1, size=10, the_index='*'):
        body = {
            "from": page,
            "size": size,
            "sort" : [
                { "created_at" : {"order" : "desc"}}
            ],
            "query": {
                "multi_match": {
                    "query": keyword,
                    "type": "best_fields",
                    "fields": ["topic", "author", "title", "text", "tags", "related"]
                }
            }
        }

        res = es.search(index=the_index, doc_type="_doc", body=body)

        if res['hits']['hits']:
            return jsonify(res['hits']['hits'])
        else:
            return "There isn't more news", 201