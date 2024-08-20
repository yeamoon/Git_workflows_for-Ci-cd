# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . /app/

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose the port that the app runs on
EXPOSE 8000

# Collect static files (optional if you manage static files differently)
RUN python manage.py collectstatic --noinput

# Run database migrations (optional; you can run these manually too)
RUN python manage.py migrate

# Start the Django app using the WSGI server (like Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend_app.wsgi:application"]
