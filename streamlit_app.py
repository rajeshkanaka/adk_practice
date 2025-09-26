"""
Streamlit UI for AI News Chatbot
Provides chat interface and news display
"""

import streamlit as st
import requests
from datetime import datetime
import time
from typing import List, Dict, Any
import json

# Configure page
st.set_page_config(
    page_title="AI News Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Backend API configuration
BACKEND_URL = "http://localhost:8000"
API_TIMEOUT = 30  # seconds

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'news_items' not in st.session_state:
    st.session_state.news_items = []
if 'last_news_update' not in st.session_state:
    st.session_state.last_news_update = None

def check_backend_health() -> bool:
    """Check if backend is running and healthy"""
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=2)
        return response.status_code == 200
    except:
        return False

def send_chat_message(message: str) -> str:
    """Send message to backend and get response"""
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/chat",
            json={"message": message},
            timeout=API_TIMEOUT
        )

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: Server returned status {response.status_code}"
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to backend server. Please ensure it's running."
    except Exception as e:
        return f"Error: {str(e)}"

def fetch_news(query: str = None) -> List[Dict[str, Any]]:
    """Fetch news from backend"""
    try:
        if query:
            response = requests.post(
                f"{BACKEND_URL}/api/news",
                params={"query": query},
                timeout=API_TIMEOUT
            )
        else:
            response = requests.get(
                f"{BACKEND_URL}/api/news/latest",
                timeout=API_TIMEOUT
            )

        if response.status_code == 200:
            return response.json()["news_items"]
        else:
            return []
    except:
        return []

def display_news_card(news_item: Dict[str, Any]):
    """Display a single news item as a card"""
    with st.container():
        st.markdown("---")
        st.subheader(news_item.get("title", "News Item"))
        st.write(news_item.get("summary", "No summary available"))

        col1, col2 = st.columns([3, 1])
        with col1:
            if news_item.get("source"):
                st.caption(f"Source: {news_item['source']}")
        with col2:
            if news_item.get("url"):
                st.markdown(f"[Read more →]({news_item['url']})")

# Main app layout
st.title("🤖 AI News Chatbot")
st.markdown("Get the latest AI news and chat about artificial intelligence developments")

# Check backend status
backend_status = check_backend_health()

if not backend_status:
    st.error("⚠️ Backend server is not running. Please start the backend server first.")
    st.info("Run `python backend_server.py` in another terminal to start the backend.")
    st.stop()

# Create two columns for layout
col_chat, col_news = st.columns([2, 1])

# Chat Interface Column
with col_chat:
    st.header("💬 Chat Assistant")

    # Display chat messages
    message_container = st.container()
    with message_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask about AI news or any AI topic..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = send_chat_message(prompt)
            st.markdown(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Rerun to update the UI
        st.rerun()

# News Display Column
with col_news:
    st.header("📰 Latest AI News")

    # Refresh news button
    col_refresh, col_search = st.columns([1, 2])

    with col_refresh:
        if st.button("🔄 Refresh", use_container_width=True):
            with st.spinner("Fetching news..."):
                st.session_state.news_items = fetch_news()
                st.session_state.last_news_update = datetime.now()
            st.rerun()

    with col_search:
        news_query = st.text_input("Search news:", placeholder="e.g., GPT, robotics", label_visibility="collapsed")
        if news_query:
            with st.spinner("Searching..."):
                st.session_state.news_items = fetch_news(news_query)
                st.session_state.last_news_update = datetime.now()

    # Auto-fetch news on first load
    if not st.session_state.news_items and not st.session_state.last_news_update:
        with st.spinner("Loading latest news..."):
            st.session_state.news_items = fetch_news()
            st.session_state.last_news_update = datetime.now()

    # Display last update time
    if st.session_state.last_news_update:
        st.caption(f"Last updated: {st.session_state.last_news_update.strftime('%H:%M:%S')}")

    # Display news items
    news_container = st.container(height=600)
    with news_container:
        if st.session_state.news_items:
            for news_item in st.session_state.news_items:
                display_news_card(news_item)
        else:
            st.info("No news items available. Click 'Refresh' to fetch latest news.")

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This AI News Chatbot helps you stay updated with the latest developments in artificial intelligence.

    **Features:**
    - 💬 Interactive chat about AI topics
    - 📰 Latest AI news feed
    - 🔍 Search specific AI topics
    - 🔄 Real-time updates

    **How to use:**
    1. Type your question in the chat
    2. Browse latest news in the sidebar
    3. Search for specific topics
    4. Refresh for latest updates
    """)

    st.divider()

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    # Connection status
    st.metric("Backend Status", "Connected ✅" if backend_status else "Disconnected ❌")

    # Footer
    st.caption("Built with Streamlit & Google ADK")