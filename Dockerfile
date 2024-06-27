# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# We DO NOT copy the rest of the application, and instead mount it as a massive
# volume.
# # Copy the rest of the application
# COPY . .

# Set environment variables (optional)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port that the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
