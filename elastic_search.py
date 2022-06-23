from elasticsearch import Elasticsearch

elasticsearch = Elasticsearch(
    'http://localhost:9200',
    basic_auth=('elastic', 'bgCTrT8w3bAApp9zBnGg'),
)

# ---- Add a new index ----
object = {
    'author': 'Raeveen Pasupathy',
    'description': 'Elasticsearch Tutorial'
}

response = (
    elasticsearch.index(
        index='misc', id=1, document=object
    )
)

print(response.get('result'))
# ---- 

# ---- Refreshing an index ---- 
elasticsearch.indices.refresh(index='misc')
# ---- 

# ---- Search for an index ---- 
response = (
    elasticsearch.search(
        index='misc',
        query={ "match_all": {} }
    )
)

print("Got %d Hits:" % response['hits']['total']['value'])

for hit in response['hits']['hits']:
    print("%(author)s: %(description)s" % hit["_source"])
# ---- 