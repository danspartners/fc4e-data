# Faircore4EOSC Compliance Assessment Toolkit data

## Step 1. Run an ElasticSearch dev container
Use the provided Docker compose file 
```
docker compose up
```

## Step 2. Install deps
```
$ npm i
```

## Step 3. Prepare data
A data.json is provided. If you want to retransform data from the original CSV, run the python script in ./data
```
$ python3 csv_to_json.py
```

## Step 4. Run the index script
Opens the data.json file and injects this into the ES container with index 'fc4e'
```
$ npm start
```