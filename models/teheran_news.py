from datetime import datetime
from elasticsearch_dsl import Document, field, InnerDoc, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import analyzer, tokenizer


class Teheran_news(Document):
    topic = Text(analyzer='snowball')

    author = Text(analyzer='snowball')

    title = Text(analyzer='snowball', fields={'raw': Keyword()})

    text = Text(analyzer='snowball')

    related = Keyword()

    tags = Keyword()

    create_at = field.Date()

    upload_at = field.Date()

    url = Keyword()

    class Index:
        name = 'teheran_news'
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }

    def save(self, *args, **kw):
            super().save(*args, **kw)