#!/bin/bash

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

# Run the ADK web interface
echo "Starting AI News Chatbot with ADK web interface..."
echo "Access the chatbot at http://localhost:8000"
adk web