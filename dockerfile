# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt && \
    python -m spacy download en_core_web_sm

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the Python script when the container launches
CMD ["python", "semantic.py"]
