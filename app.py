from flask import Flask
from flask_restful import Api

from resources.news import Base, News, News_list, Create_sk_article, Create_tn_article

app = Flask(__name__)

api = Api(app)

api.add_resource(Base, "/")
api.add_resource(News, "/news/<string:news_id>")
api.add_resource(News_list, "/news-list")
api.add_resource(Create_sk_article, "/create-somos-kudasai-article")
api.add_resource(Create_tn_article, "/create-teheran-news-article")

if __name__ == "__main__":
    app.run(debug=True)