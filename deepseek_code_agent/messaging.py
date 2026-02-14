"""DeepSeek Code Agent - Inter-agent messaging."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Message:
    """Represents a message between agents."""
    
    from_agent: str
    to_agent: str
    content: str
    id: str = field(default_factory=lambda: f"msg_{uuid.uuid4().hex[:8]}")
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    metadata: dict[str, Any] = field(default_factory=dict)


class MessageBus:
    """Message bus for inter-agent communication."""
    
    def __init__(self) -> None:
        self.messages: list[Message] = []
    
    def publish(self, message: Message) -> None:
        """Publish a message."""
        self.messages.append(message)
    
    def subscribe(self, agent_id: str) -> list[Message]:
        """Get messages for an agent."""
        return [m for m in self.messages if m.to_agent == agent_id]
    
    def clear(self) -> None:
        """Clear all messages."""
        self.messages.clear()
