#!/bin/bash

# Script to run the Streamlit frontend

echo "Starting AI News Chatbot Streamlit UI..."
echo "UI will be available at http://localhost:8501"
echo ""
echo "Make sure the backend server is running first!"
echo "Run './run_backend.sh' in another terminal"
echo ""
echo "Press Ctrl+C to stop the application"

# Run the Streamlit app
streamlit run streamlit_app.py