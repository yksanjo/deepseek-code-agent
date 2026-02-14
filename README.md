# DeepSeek Code Agent

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Multi-Agent Framework for AI Coding** - Coordinate multiple AI agents for complex tasks.

**多智能体框架 for AI 编程** - 协调多个 AI 智能体完成复杂任务。

<p align="center">
  <img src="https://img.shields.io/badge/Multi--Agent-blue" alt="Multi-Agent">
  <img src="https://img.shields.io/badge/Orchestration-orange" alt="Orchestration">
  <img src="https://img.shields.io/badge/Parallel-green" alt="Parallel">
</p>

```
  ____                 ____            _       _
 |  _ \  ___  ___ _ __/ ___|  ___  ___| | __ | |
 | | | |/ _ \/ _ \ '_ \___ \ / _ \/ _ \ |/ /| |
 | |_| |  __/  __/ |_) |__) |  __/  __/   < |_|
 |____/ \___|\___| .__/____/ \___|\___|_|\_\|_|
    ____          |_|  _    | |      _ 
   / ___|___   __| | __|  | |_____| |_ _ __ 
  | |   / _ \ / _` | '_ \ '_ \| __| __| '__|
  | |__| (_) | (_| | |_) | | | |_| | | | 
   \____\___/ \__,_|\__/\__/_|\__|\__|_| |_|
```

---

## Why DeepSeek Code Agent?

<details>
<summary>🇨🇳 中文</summary>

- **多智能体**: 协调多个专业智能体
- **并行执行**: 同时运行多个任务
- **任务分解**: 复杂问题分解为子任务
- **协作**: 智能体之间可以通信协作
- **可扩展**: 轻松添加新的智能体类型

### 主要功能

| 功能 | 描述 |
|------|------|
| **智能体编排** | 协调多个智能体 |
| **并行执行** | 同时运行多个任务 |
| **任务队列** | 任务优先级和队列管理 |
| **通信** | 智能体间消息传递 |
| **监控** | 实时状态监控 |

</details>

<details open>
<summary>🇺🇸 English</summary>

- **Multi-Agent**: Coordinate multiple specialized agents
- **Parallel Execution**: Run tasks concurrently
- **Task Decomposition**: Break complex problems into subtasks
- **Collaboration**: Agents can communicate with each other
- **Extensible**: Easily add new agent types

## Features

| Feature | Description |
|---------|-------------|
| **Agent Orchestration** | Coordinate multiple agents |
| **Parallel Execution** | Run tasks concurrently |
| **Task Queue** | Priority and queue management |
| **Messaging** | Inter-agent communication |
| **Monitoring** | Real-time status tracking |

</details>

## Installation

```bash
git clone https://github.com/yksanjo/deepseek-code-agent.git
cd deepseek-code-agent
pip install -e .
```

## Quick Start

### Basic Agent

```python
from deepseek_code_agent import Agent, Task

# Create an agent
coder = Agent(
    name="coder",
    role="Senior Python Developer",
    tools=["read_file", "write_file", "bash"]
)

# Run a task
task = Task(description="Create a REST API")
result = coder.run(task)
print(result)
```

### Multi-Agent Team

```python
from deepseek_code_agent import Agent, Team, Task

# Create specialized agents
planner = Agent(name="planner", role="Technical Lead")
coder = Agent(name="coder", role="Python Developer")
reviewer = Agent(name="reviewer", role="Code Reviewer")

# Create team
team = Team(agents=[planner, coder, reviewer])

# Assign complex task
task = Task(
    description="Build a todo app with API",
    decompose=True  # Break into subtasks
)

result = team.run(task)
```

### Parallel Execution

```python
from deepseek_code_agent import Agent, TaskQueue

# Create agents
agents = [Agent(name=f"agent_{i}") for i in range(3)]

# Create queue
queue = TaskQueue(agents)

# Add tasks
queue.add_task(Task(description="Fix bug 1"))
queue.add_task(Task(description="Fix bug 2"))
queue.add_task(Task(description="Fix bug 3"))

# Run in parallel
results = queue.run()
```

## Architecture

```
deepseek_code_agent/
├── __init__.py           # Main exports
├── agent.py              # Base Agent class
├── team.py               # Team orchestration
├── task.py               # Task definitions
├── queue.py              # Task queue
├── messaging.py          # Inter-agent messaging
├── monitor.py            # Status monitoring
└── examples/
    └── team.py           # Example implementations
```

## Agent Types

### Coder Agent

```python
from deepseek_code_agent.agents import CoderAgent

coder = CoderAgent(
    name="main-coder",
    language="python",
    tools=["read_file", "write_file", "edit_file"]
)
```

### Reviewer Agent

```python
from deepseek_code_agent.agents import ReviewerAgent

reviewer = ReviewerAgent(
    name="code-reviewer",
    strict=True
)
```

### Planner Agent

```python
from deepseek_code_agent.agents import PlannerAgent

planner = PlannerAgent(
    name="architect",
    breakdown_style="detailed"
)
```

## Examples

### Code Review Team

```python
from deepseek_code_agent import Agent, Team

# Create review team
reviewer = Agent(name="reviewer", role="Security Expert")
tester = Agent(name="tester", role="QA Engineer")

team = Team([reviewer, tester])

# Run code review
result = team.run("Review authentication module")
```

### Full Stack Development

```python
from deepseek_code_agent import Agent, Team

# Create full stack team
backend = Agent(name="backend", role="API Developer")
frontend = Agent(name="frontend", role="UI Developer")
db = Agent(name="db", role="Database Engineer")

team = Team([backend, frontend, db])
team.run("Build user authentication system")
```

### Bug Fix Sprint

```python
from deepseek_code_agent import Agent, TaskQueue

# Create bug fixing team
agents = [Agent(name=f"fixer_{i}") for i in range(5)]
queue = TaskQueue(agents)

# Add bugs
for bug in bug_list:
    queue.add_task(Task(description=f"Fix: {bug}"))

# Parallel fix
results = queue.run(parallel=True)
```

## Task Decomposition

```python
from deepseek_code_agent import Task

task = Task(
    description="Build e-commerce platform",
    decompose=True,
    max_depth=3,
    strategies=["by_layer", "by_feature"]
)

# Automatically breaks down into:
# - Frontend tasks
# - Backend tasks
# - Database tasks
# - DevOps tasks
```

## Inter-Agent Communication

```python
from deepseek_code_agent import Agent, Message

# Create agents
agent_a = Agent(name="A")
agent_b = Agent(name="B")

# Send message
agent_a.send_to(agent_b, "Need the API spec")

# Receive
message = agent_b.receive()
```

## Monitoring

```python
from deepseek_code_agent import Monitor

monitor = Monitor()

# Track agents
monitor.track(agent1)
monitor.track(agent2)

# Get status
status = monitor.status()
print(status)
# {
#   "agent1": {"status": "running", "tasks": 3},
#   "agent2": {"status": "waiting", "tasks": 1}
# }
```

## Configuration

```python
from deepseek_code_agent import Config

config = Config(
    max_agents=10,
    timeout=300,
    retry_attempts=3,
    parallel_limit=5,
)
```

## Use Cases

- **Code Review**: Multiple reviewers with different specialties
- **Full Stack Dev**: Frontend + Backend + DB agents working together
- **Bug Hunts**: Parallel bug fixing by multiple agents
- **Refactoring**: Coordinated code restructuring
- **Testing**: Generate and run tests in parallel
- **Documentation**: Multiple docs generated concurrently

## License

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  <b>Star this repo if you find it useful!</b>
</p>
