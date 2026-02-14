"""DeepSeek Code Agent - Task queue."""

import asyncio
from dataclasses import dataclass, field
from typing import Any

from .agent import Agent
from .task import Task, TaskResult


@dataclass
class TaskQueue:
    """Queue for managing tasks across multiple agents."""
    
    agents: list[Agent] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)
    parallel: bool = False
    
    def add_task(self, task: Task) -> None:
        """Add task to queue."""
        self.tasks.append(task)
    
    def run(self) -> list[TaskResult]:
        """Run all tasks."""
        results = []
        
        if self.parallel:
            # Run tasks in parallel
            for task in self.tasks:
                agent = self._get_available_agent()
                if agent:
                    result = agent.run(task)
                    results.append(result)
        else:
            # Run sequentially
            for task in self.tasks:
                agent = self._get_available_agent()
                if agent:
                    result = agent.run(task)
                    results.append(result)
        
        return results
    
    def _get_available_agent(self) -> Agent | None:
        """Get an available agent."""
        for agent in self.agents:
            if agent.status == "idle":
                return agent
        return self.agents[0] if self.agents else None
