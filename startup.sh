#!/bin/bash
# This script starts the AI Query Backend MVP.

set -e

# Source environment variables
source .env

# Start the FastAPI application
echo "Starting FastAPI application..."
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

# Check if the application is running
echo "Checking if application is running..."
if [ $(pgrep -f "uvicorn api.main:app") ]; then
    echo "Application started successfully."
else
    echo "Error: Failed to start application."
    exit 1
fi