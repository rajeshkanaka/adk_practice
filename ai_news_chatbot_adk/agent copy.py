"""
AI News Chatbot Agent

This module defines an AI News Agent using Google's Agent Development Kit (ADK).
The agent is designed to search the web for the latest AI news and provide
informative responses to user queries.
"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# Define the model to use
MODEL = "gemini-2.5-flash"

# Create the AI News Agent
ai_news_agent = LlmAgent(
    name="ai_news_agent",
    model=MODEL,
    description="Agent that provides the latest AI news and information",
    instruction="""You are an AI news assistant. Your primary role is to provide accurate,
    up-to-date information about artificial intelligence developments, news, and trends.

    When asked about AI news or developments:
    1. Use the google_search tool to find the most recent and relevant information
    2. Provide concise but informative responses
    3. Include sources or references when appropriate
    4. If the information might be outdated, acknowledge this limitation

    Always maintain a helpful, informative tone and focus on delivering factual information.
    """,
    tools=[google_search]
)

# This is required for ADK to discover the agent
root_agent = ai_news_agent

# For testing the agent directly
if __name__ == "__main__":
    print("AI News Agent created successfully!")
    print(f"Agent name: {root_agent.name}")
    print(f"Agent model: {root_agent.model}")
    print(f"Agent tools: {[type(tool).__name__ for tool in root_agent.tools]}")