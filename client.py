from elasticsearch import Elasticsearch

def get_es_client():
    return Elasticsearch("http://localhost:9200")

es_client = get_es_client()
