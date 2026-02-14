"""DeepSeek Code Agent - Multi-Agent Framework."""

from .agent import Agent
from .team import Team
from .task import Task, TaskResult
from .queue import TaskQueue
from .messaging import Message
from .monitor import Monitor

__version__ = "0.1.0"
__all__ = [
    "Agent",
    "Team", 
    "Task",
    "TaskResult",
    "TaskQueue",
    "Message",
    "Monitor",
]
