# Faircore4EOSC Compliance Assessment Toolkit data

## Step 1. Run an ElasticSearch dev container
Use the provided Docker compose file 
```
docker compose up
```
## Step 2. Run the index script
Opens the source CSV file and injects this into the ES container with index 'fc4e'
```
$ python3 run.py
```