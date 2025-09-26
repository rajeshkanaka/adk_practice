"""
AI News Chatbot Agent Package

This package provides a chatbot that can search the web for the latest AI news
and provide informative responses to user queries using Google's Agent Development Kit.

from . import agent: This line performs a relative import, telling Python to look for a module named agent (which corresponds to agent.py) within the current package (personal-assistant). This simple line ensures that when ADK tries to load your personal-assistant agent, it can find and initialize the root_agent defined in agent.py. Even if empty, the presence of __init__.py is what makes the directory a Python package.
"""

from .agent import root_agent

__all__ = ["root_agent"]