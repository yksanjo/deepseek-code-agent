"""DeepSeek Code Agent - Base Agent implementation."""

import uuid
from dataclasses import dataclass, field
from typing import Any

from .task import Task, TaskResult
from .messaging import Message


@dataclass
class Agent:
    """Base Agent class for multi-agent framework."""
    
    name: str
    role: str = "General Assistant"
    tools: list[str] = field(default_factory=list)
    model: str = "deepseek-chat"
    max_turns: int = 50
    
    def __post_init__(self) -> None:
        self.id = f"agent_{uuid.uuid4().hex[:8]}"
        self.status = "idle"
        self.current_task: Task | None = None
        self.inbox: list[Message] = []
        self.outbox: list[Message] = []
    
    def run(self, task: Task) -> TaskResult:
        """Run a task."""
        self.status = "running"
        self.current_task = task
        
        # Simulate task execution
        result = TaskResult(
            task_id=task.id,
            agent_id=self.id,
            success=True,
            output=f"Agent {self.name} completed: {task.description}",
        )
        
        self.status = "idle"
        self.current_task = None
        return result
    
    def send_to(self, other: "Agent", content: str) -> None:
        """Send message to another agent."""
        msg = Message(
            from_agent=self.id,
            to_agent=other.id,
            content=content,
        )
        self.outbox.append(msg)
    
    def receive(self) -> Message | None:
        """Receive a message."""
        if self.inbox:
            return self.inbox.pop(0)
        return None
    
    def can_handle(self, task: Task) -> bool:
        """Check if agent can handle the task."""
        return True
    
    def __repr__(self) -> str:
        return f"Agent(name={self.name}, role={self.role}, status={self.status})"
