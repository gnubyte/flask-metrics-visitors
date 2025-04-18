FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project context (including parent directory)
COPY . /flask_metrics_visitors

# Install the local package
RUN pip install -e /flask_metrics_visitors

# Copy the demo app files
COPY demo/app/ .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"] 