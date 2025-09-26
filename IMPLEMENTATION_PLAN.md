# AI News Chatbot - Streamlit Integration Implementation Plan

## Architecture Overview
```
[Streamlit UI (Port 8501)]  <--REST API--> [FastAPI Backend (Port 8000)]
     |                                            |
     ├── Chat Interface                           ├── ADK Agent
     └── News Display Panel                       └── Google Search Tool
```

## Stage 1: Backend API Server
**Goal**: Create FastAPI server to wrap ADK agent with REST endpoints
**Success Criteria**:
- `/chat` endpoint accepts messages and returns AI responses
- `/news` endpoint returns latest AI news
- Server runs on port 8000
**Tests**: Can send POST to /chat and get response
**Status**: Complete ✓

## Stage 2: Streamlit Chat UI
**Goal**: Create clean Streamlit chat interface
**Success Criteria**:
- Chat history displayed properly
- Input field for user messages
- Real-time response display
- Responsive design
**Tests**: Can send messages and see responses
**Status**: Complete ✓

## Stage 3: News Display Component
**Goal**: Add news panel to Streamlit UI
**Success Criteria**:
- Displays latest AI news in cards/list format
- Auto-refreshes periodically
- Clickable links to sources
**Tests**: News items display and update
**Status**: Complete ✓

## Stage 4: Integration & Polish
**Goal**: Complete integration with error handling
**Success Criteria**:
- Graceful error handling
- Loading states
- Clear startup instructions
- Docker support (optional)
**Tests**: System works end-to-end
**Status**: Complete ✓

## Key Design Decisions

### Why This Architecture?
1. **Separation of Concerns**: Backend handles ADK logic, frontend handles UI
2. **Scalability**: Can scale backend independently
3. **Industry Standard**: REST API pattern is well-understood
4. **Simple Deployment**: Two simple processes to manage

### Technology Choices
- **FastAPI**: Fast, modern, automatic OpenAPI docs
- **Streamlit**: Rapid prototyping, built-in chat components
- **REST over WebSocket**: Simpler, sufficient for chat use case

### Code Principles
- Minimal dependencies
- Clear error messages
- Type hints throughout
- Defensive programming
- Configuration via environment variables