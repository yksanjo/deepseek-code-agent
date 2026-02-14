"""DeepSeek Code Agent - Team orchestration."""

from dataclasses import dataclass, field
from typing import Any

from .agent import Agent
from .task import Task, TaskResult


@dataclass
class Team:
    """Team of agents that can collaborate on tasks."""
    
    agents: list[Agent] = field(default_factory=list)
    name: str = "Team"
    
    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the team."""
        self.agents.append(agent)
    
    def remove_agent(self, agent: Agent) -> None:
        """Remove an agent from the team."""
        self.agents.remove(agent)
    
    def run(self, task: Task) -> TaskResult:
        """Run a task with the team."""
        if task.decompose:
            subtasks = self._decompose_task(task)
            results = []
            for subtask in subtasks:
                agent = self._select_agent(subtask)
                result = agent.run(subtask)
                results.append(result)
            return TaskResult(
                task_id=task.id,
                agent_id=self.name,
                success=True,
                output=f"Team completed {len(results)} subtasks",
            )
        
        agent = self._select_agent(task)
        return agent.run(task)
    
    def _decompose_task(self, task: Task) -> list[Task]:
        """Decompose a task into subtasks."""
        # Simple decomposition - in real implementation, use AI
        return [Task(description=f"Part of: {task.description}") for _ in range(3)]
    
    def _select_agent(self, task: Task) -> Agent:
        """Select best agent for task."""
        for agent in self.agents:
            if agent.can_handle(task):
                return agent
        return self.agents[0]
    
    def __repr__(self) -> str:
        return f"Team(name={self.name}, agents={len(self.agents)})"
