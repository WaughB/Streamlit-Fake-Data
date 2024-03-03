# Streamlit Fake Data

This project lets the user create fake data based on a certain schema. 

## How to run 

### Bare metal

__Important notes__ Preferred method for now. Still working on persisting the data for Docker and docker-compose integration.  

To start the Streamlit application, 

```
streamlit run app.py
```

To start the Flask app, 

```
python run api.py
```

### Docker

__Important notes__ Still working out the volumes to persist the data after the containers are torn down. Presently, any saved data or schema would disappear after taking down the Docker container. 

To run the containerized version of Streamlit: 

```
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

To start the containerized version of Flask:  

```
docker build -t flask-api .
docker run -p 5000:5000 flask-api

```


### Docker-compose 

TODO


## Networking information

The Streamlit app runs on `http://localhost:8501`. The Flask API runs on `http://127.0.0.1:5000`. 