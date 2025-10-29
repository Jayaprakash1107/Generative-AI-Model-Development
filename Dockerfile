# Start from an official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/hf_cache && chmod 777 /app/hf_cache
ENV TRANSFORMERS_CACHE=/app/hf_cache

# Copy all your project files (main.py, etc.) into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# The command to run your app
# We use 0.0.0.0 to make it accessible outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]