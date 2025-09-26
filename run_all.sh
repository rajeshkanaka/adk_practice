#!/bin/bash

# Script to run both backend and frontend services

# Function to clean up background processes on exit
cleanup() {
    echo ""
    echo "Shutting down services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up trap to cleanup on script exit
trap cleanup EXIT INT TERM

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please create one based on .env.example"
    exit 1
fi

# Source the .env file
source .env

# Check if API key is set
if [ -z "$GOOGLE_API_KEY" ] || [ "$GOOGLE_API_KEY" = "your_api_key_here" ]; then
    echo "Error: Please set your Google API key in the .env file"
    exit 1
fi

# Export the API key
export GOOGLE_API_KEY

echo "Starting AI News Chatbot Services..."
echo "======================================="

# Start backend server in background
echo "Starting backend server..."
python backend_server.py &
BACKEND_PID=$!

# Wait for backend to start
echo "Waiting for backend to initialize..."
sleep 5

# Check if backend is running
if ! kill -0 $BACKEND_PID 2>/dev/null; then
    echo "Error: Backend failed to start"
    exit 1
fi

echo "Backend started successfully at http://localhost:8000"
echo ""

# Start frontend in background
echo "Starting Streamlit UI..."
streamlit run streamlit_app.py --server.headless true &
FRONTEND_PID=$!

# Wait for frontend to start
sleep 3

echo ""
echo "======================================="
echo "AI News Chatbot is running!"
echo ""
echo "🌐 Streamlit UI: http://localhost:8501"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
echo "======================================="

# Wait for processes
wait