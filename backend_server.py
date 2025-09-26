"""
Backend API Server for AI News Chatbot
Provides REST API endpoints for the ADK agent
"""

import os
import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Suppress noisy google-adk registry INFO logs during startup
logging.getLogger("google_adk").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Import ADK agent
from ai_news_chatbot_adk.agent import root_agent, query

# Pydantic models for request/response
class ChatMessage(BaseModel):
    message: str = Field(..., description="User message to the chatbot")

class ChatResponse(BaseModel):
    response: str = Field(..., description="AI assistant response")
    timestamp: datetime = Field(default_factory=datetime.now)

class NewsItem(BaseModel):
    title: str
    summary: str
    source: Optional[str] = None
    url: Optional[str] = None
    published_date: Optional[str] = None

class NewsResponse(BaseModel):
    news_items: List[NewsItem]
    query: str
    timestamp: datetime = Field(default_factory=datetime.now)

# Create FastAPI app
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting AI News Chatbot Backend Server")
    if not os.getenv("GOOGLE_API_KEY"):
        logger.warning("GOOGLE_API_KEY not found in environment variables")
    yield
    # Shutdown
    logger.info("Shutting down AI News Chatbot Backend Server")

app = FastAPI(
    title="AI News Chatbot API",
    description="Backend API for AI News Chatbot with ADK integration",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "service": "AI News Chatbot Backend",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "chat": "/api/chat",
            "news": "/api/news",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "agent_status": "ready" if root_agent else "not initialized"
    }

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(message: ChatMessage):
    """
    Chat endpoint to interact with the AI News Agent
    """
    try:
        # Run agent query in executor to avoid blocking
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            query,
            message.message
        )

        # Extract text response (ADK returns structured output)
        response_text = response.text if hasattr(response, 'text') else str(response)

        return ChatResponse(
            response=response_text,
            timestamp=datetime.now()
        )

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")

@app.post("/api/news", response_model=NewsResponse)
async def get_news(query: str = "latest AI news today"):
    """
    Get latest AI news based on query
    """
    try:
        # Create a specific query for news retrieval
        news_query = f"Search for the latest news about: {query}. Provide a list of recent news items with titles and summaries."

        # Run agent query
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            query,
            news_query
        )

        response_text = response.text if hasattr(response, 'text') else str(response)

        # Mock parsing - in reality, you'd parse the structured response
        news_items = []
        lines = response_text.split('\n')
        current_item = {}

        for line in lines:
            line = line.strip()
            if line.startswith('•') or line.startswith('-') or line.startswith('*'):
                if current_item:
                    news_items.append(NewsItem(
                        title=current_item.get('title', 'Untitled'),
                        summary=current_item.get('summary', line[1:].strip()),
                        source=current_item.get('source'),
                        url=current_item.get('url')
                    ))
                current_item = {'title': line[1:].strip(), 'summary': ''}
            elif current_item:
                current_item['summary'] += ' ' + line

        # Add last item if exists
        if current_item:
            news_items.append(NewsItem(
                title=current_item.get('title', 'Latest AI News'),
                summary=current_item.get('summary', response_text[:200]),
                source="AI News Agent"
            ))

        # If no structured items found, create one from response
        if not news_items:
            news_items = [NewsItem(
                title="AI News Update",
                summary=response_text[:500] + "..." if len(response_text) > 500 else response_text,
                source="AI News Agent"
            )]

        return NewsResponse(
            news_items=news_items,
            query=query,
            timestamp=datetime.now()
        )

    except Exception as e:
        logger.error(f"Error fetching news: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching news: {str(e)}")

@app.get("/api/news/latest")
async def get_latest_news():
    """
    Convenience endpoint for getting latest AI news without specifying query
    """
    return await get_news("latest artificial intelligence news and breakthroughs today")

if __name__ == "__main__":
    import uvicorn

    # Run the server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
