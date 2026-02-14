"""DeepSeek Code Agent - Monitoring."""

from dataclasses import dataclass, field
from typing import Any

from .agent import Agent


@dataclass
class Monitor:
    """Monitor for tracking agent status."""
    
    agents: dict[str, Agent] = field(default_factory=dict)
    
    def track(self, agent: Agent) -> None:
        """Track an agent."""
        self.agents[agent.id] = agent
    
    def untrack(self, agent: Agent) -> None:
        """Stop tracking an agent."""
        if agent.id in self.agents:
            del self.agents[agent.id]
    
    def status(self) -> dict[str, dict[str, Any]]:
        """Get status of all tracked agents."""
        return {
            agent.id: {
                "name": agent.name,
                "role": agent.role,
                "status": agent.status,
                "current_task": agent.current_task.description if agent.current_task else None,
            }
            for agent in self.agents.values()
        }
    
    def get_idle_agents(self) -> list[Agent]:
        """Get list of idle agents."""
        return [a for a in self.agents.values() if a.status == "idle"]
    
    def get_running_agents(self) -> list[Agent]:
        """Get list of running agents."""
        return [a for a in self.agents.values() if a.status == "running"]
