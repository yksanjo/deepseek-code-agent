"""DeepSeek Code Agent - Task definitions."""

import uuid
from dataclasses import dataclass, field
from typing import Any
from enum import Enum


class TaskStatus(Enum):
    """Task status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    """Represents a task to be executed by an agent."""
    
    description: str
    id: str = field(default_factory=lambda: f"task_{uuid.uuid4().hex[:8]}")
    priority: int = 0
    decompose: bool = False
    max_depth: int = 3
    strategies: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    
    status: TaskStatus = TaskStatus.PENDING
    
    def __post_init__(self) -> None:
        if not self.strategies:
            self.strategies = ["by_feature"]


@dataclass
class TaskResult:
    """Result of task execution."""
    
    task_id: str
    agent_id: str
    success: bool
    output: str
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
