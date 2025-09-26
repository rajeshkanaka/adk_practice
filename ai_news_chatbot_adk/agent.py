"""Basic AI News agent definition for student exercises."""

import asyncio
import uuid
from dataclasses import dataclass
from typing import Optional

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.tools import google_search
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

MODEL = "gemini-2.5-flash"

root_agent = LlmAgent(
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
    tools=[google_search],
)

_APP_NAME = "ai-news-chatbot"
_DEFAULT_USER = "student"


@dataclass
class AgentResponse:
    """Minimal response object matching the older samples."""

    text: str

    def __str__(self) -> str:  # pragma: no cover - convenience fallback
        return self.text


def _extract_text(content: Optional[types.Content]) -> str:
    if not content or not content.parts:
        return ""
    lines: list[str] = []
    for part in content.parts:
        if part.text:
            lines.append(part.text.strip())
    return "\n".join(line for line in lines if line)


async def _run_agent(prompt: str) -> AgentResponse:
    session_service = InMemorySessionService()
    runner = Runner(
        app_name=_APP_NAME,
        agent=root_agent,
        session_service=session_service,
        artifact_service=InMemoryArtifactService(),
        memory_service=InMemoryMemoryService(),
    )

    session_id = str(uuid.uuid4())
    await session_service.create_session(
        app_name=_APP_NAME,
        user_id=_DEFAULT_USER,
        session_id=session_id,
    )

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)],
    )

    final_text = ""
    async for event in runner.run_async(
        user_id=_DEFAULT_USER,
        session_id=session_id,
        new_message=user_message,
    ):
        if event.author == root_agent.name and event.is_final_response():
            final_text = _extract_text(event.content)

    return AgentResponse(text=final_text.strip())


async def query_async(prompt: str) -> AgentResponse:
    """Async helper for callers already running an event loop."""
    return await _run_agent(prompt)


def query(prompt: str) -> AgentResponse:
    """Synchronous helper used by the FastAPI backend and tutorials."""
    return asyncio.run(_run_agent(prompt))


if __name__ == "__main__":
    print("AI News Agent ready for student projects!")
    sample = query("What are the latest AI news headlines?")
    print(sample.text)
