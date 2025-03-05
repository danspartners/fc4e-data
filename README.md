# Faircore4EOSC Compliance Assessment Toolkit data

## Step 1. Run an ElasticSearch dev container
Use the provided Docker compose file 
```sh
docker compose up
```
## Step 2. Install dependencies
```sh
pip install -r requirements.txt
```
## Step 3. Create and fill index
Opens the source CSV file and injects this into the ES container.
```sh
python main.py
```

If needed, you can set some optional environment variables:

- **`ELASTICSEARCH_URL`**: The URL of your Elasticsearch server, default to `"http://localhost:9200"`.
- **`INDEX_NAME`**: ElasticSearch index you want to create/use, defaults to **4cfe**
- **`FILE_PATH`**: Points to CSV file location, defaults to **./data/Elastic_JSON.csv** included in this repo.
  
```sh
ELASTICSEARCH_URL="http://localhost:9200" \
INDEX_NAME="4cfe" \
FILE_PATH="./data/Elastic_JSON.csv" \
python main.py
```