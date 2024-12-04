# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy and install dependencies
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the application
COPY app/ .

# Define the default command
CMD ["python", "main.py"]
