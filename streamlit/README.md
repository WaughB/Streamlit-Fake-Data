# Streamlit Fake Data

This project lets the user create fake data based on a certain schema. 

## How to run 

To start the Streamlit application, 

```
streamlit run app.py
```

To run the containerized version of this: 

```
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

## Networking information

The Streamlit app runs on `http://localhost:8501`.