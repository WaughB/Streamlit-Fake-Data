# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /streamlit

# Copy the current directory contents into the container at /streamlit
COPY . /streamlit

# Install any needed packages specified in requirements.txt
COPY requirements.txt /streamlit/
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run Streamlit app when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
