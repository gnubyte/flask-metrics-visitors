#!/bin/bash

# Stop and remove existing container if it exists
echo "Cleaning up existing container..."
docker stop flask-metrics-demo 2>/dev/null || true
docker rm flask-metrics-demo 2>/dev/null || true

# Build the Docker image from the parent directory to include the package
echo "Building Docker image..."
cd .. && docker build -t flask-metrics-demo -f demo/Dockerfile .

# Run the container
echo "Starting container..."
docker run -d -p 5000:5000 --name flask-metrics-demo flask-metrics-demo

echo "Demo is running at http://localhost:5000"
echo "Login credentials: admin / admin"
echo "Metrics dashboard: http://localhost:5000/metrics"
echo ""
echo "To stop the demo, run: ./demo.sh stop"
echo "To view logs, run: docker logs -f flask-metrics-demo" 