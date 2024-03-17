# Use an official Python base image
FROM python:3.10-slim

# Defines the working directory in the container
WORKDIR /app

# Copy the required Python and YAML code files to the working directory
COPY app.py config.yaml requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask application is running
EXPOSE 5002

# Command to launch the Flask application
CMD ["python", "app.py"]
