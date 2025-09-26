# AI News Chatbot - Setup & Usage Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
Make sure your `.env` file contains your Google API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Run the Application

**Option A: Run Everything Together (Recommended)**
```bash
./run_all.sh
```

**Option B: Run Services Separately**

Terminal 1 - Backend:
```bash
./run_backend.sh
```

Terminal 2 - Frontend:
```bash
./run_frontend.sh
```

### 4. Access the Application
- **Streamlit UI**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Architecture Overview

```
┌─────────────────────┐         ┌──────────────────────┐
│   Streamlit UI      │  REST   │   FastAPI Backend    │
│   (Port 8501)       │ <────>  │   (Port 8000)        │
│                     │         │                      │
│ • Chat Interface    │         │ • /api/chat endpoint │
│ • News Display      │         │ • /api/news endpoint │
│ • Search Feature    │         │ • ADK Agent          │
└─────────────────────┘         └──────────────────────┘
```

## Features

### Chat Interface
- Real-time chat with AI assistant
- Persistent conversation history
- Automatic response streaming

### News Display
- Latest AI news in sidebar
- Search specific topics
- Auto-refresh capability
- Clean card-based layout

### Backend API
- RESTful endpoints
- Automatic OpenAPI documentation
- Health check endpoint
- CORS enabled for frontend

## File Structure

```
ai_news_chatbot_adk/
├── backend_server.py      # FastAPI backend with ADK agent
├── streamlit_app.py        # Streamlit frontend UI
├── run_backend.sh          # Backend launch script
├── run_frontend.sh         # Frontend launch script
├── run_all.sh             # Combined launch script
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
└── ai_news_chatbot_adk/
    └── agent.py           # ADK agent definition
```

## API Endpoints

### POST `/api/chat`
Send a message and receive AI response
```json
Request:  {"message": "What's new in AI?"}
Response: {"response": "...", "timestamp": "..."}
```

### POST `/api/news`
Get news based on query
```json
Request:  {"query": "GPT updates"}
Response: {"news_items": [...], "query": "...", "timestamp": "..."}
```

### GET `/api/news/latest`
Get latest AI news without query

### GET `/health`
Check backend status

## Troubleshooting

### Backend won't start
- Check if `.env` file exists and contains valid API key
- Ensure port 8000 is not in use
- Check Python version (3.8+ required)

### Frontend can't connect to backend
- Ensure backend is running first
- Check if port 8000 is accessible
- Verify firewall settings

### No news displayed
- Check internet connection
- Verify Google API key is valid
- Check backend logs for errors

## Development Tips

### Adding New Features
1. Backend changes go in `backend_server.py`
2. UI changes go in `streamlit_app.py`
3. Agent modifications in `ai_news_chatbot_adk/agent.py`

### Testing
- Backend API: Visit http://localhost:8000/docs
- Use FastAPI's interactive documentation to test endpoints
- Monitor console logs for debugging

### Performance
- Backend uses async/await for non-blocking operations
- Streamlit caches responses when possible
- News fetching runs in background

## Stop Services

Press `Ctrl+C` in the terminal running the services, or:

```bash
# Find processes
ps aux | grep -E "streamlit|uvicorn"

# Kill processes
pkill -f streamlit
pkill -f uvicorn
```