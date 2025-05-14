from elasticsearch import Elasticsearch
import os

def get_es_client():
    es_url = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")  # Default to localhost if not set
    return Elasticsearch(es_url)

es_client = get_es_client()

mappings = {
    "mappings": {
        "properties": {
            "id": {"type": "keyword"},
            "api": {"type": "keyword"},
            "mpa": {"type": "keyword"},
            "count": {"type": "integer"},
            "gupri": {"type": "keyword"},
            "label": {"type": "text"},
            "entity": {"type": "keyword"},
            "scheme": {"type": "keyword"},
            "status": {"type": "keyword"},
            "unique": {"type": "keyword"},
            "coverage": {"type": "keyword"},
            "managers": {"type": "integer"},
            "provider": {"type": "keyword"},
            "standard": {"type": "keyword"},
            "authority": {"type": "keyword"},
            "countries": {
                "type": "object",
                "properties": {
                    "name": {"type": "keyword"},
                    "iso": {"type": "keyword"},
                    "location": {"type": "geo_point"}
                }
            },
            "identifier": {
                "type": "keyword",
                "fields": {
                    "normalized": {
                        "type": "keyword",
                        "normalizer": "lowercase"
                    }
                }
            },
            "persistent": {"type": "keyword"},
            "resolvable": {"type": "keyword"},
            "start_date": { 
                "type": "date",
                "format": "yyyy||yyyy-MM-dd"
            },
            "description": {"type": "text"},
            "availability": {"type": "keyword"},
            "disciplinary": {"type": "keyword"},
            "metaresolvers": {"type": "keyword"},
            "namespace_type": {"type": "keyword"},
            "recommended_by": {"type": "integer"},
            "globally_unique": {"type": "boolean"},
            "identifier_type": {"type": "keyword"},
            "resolution_type": {"type": "keyword"},
            "number_of_resolvers": {"type": "integer"},
            "resolution_topology": {"type": "keyword"}
        }
    },
    "settings": {
        "analysis": {
            "normalizer": {
                "lowercase": {
                    "type": "custom",
                    "filter": ["lowercase"]
                }
            }
        }
    }
}
