# Streamlit Fake Data

This project lets the user create fake data based on a certain schema. 

## How to run 

To start the Flask app, 

```
python api.py
```

To start the containerized version,  

```
docker build -t flask-api .
docker run -p 5000:5000 flask-api

```

## Networking information

The Flask API runs on `http://127.0.0.1:5000`. To get the data, please go to: `http://127.0.0.1:5000/get_data`