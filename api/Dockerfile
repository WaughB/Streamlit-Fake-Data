# Use an official lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /api

# Copy the Flask application and any other required files into the container
COPY . /api

# Install the Python packages needed for the Flask app
COPY requirements.txt /api/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "api.py"]
