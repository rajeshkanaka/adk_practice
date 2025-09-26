#!/bin/bash

# Script to run the backend API server

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please create one based on .env.example"
    exit 1
fi

# Source the .env file to get the API key
source .env

# Check if API key is set
if [ -z "$GOOGLE_API_KEY" ] || [ "$GOOGLE_API_KEY" = "your_api_key_here" ]; then
    echo "Error: Please set your Google API key in the .env file"
    exit 1
fi

# Export the API key for the Python process
export GOOGLE_API_KEY

echo "Starting AI News Chatbot Backend Server..."
echo "Backend will be available at http://localhost:8000"
echo "API documentation available at http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"

# Run the backend server
python backend_server.py