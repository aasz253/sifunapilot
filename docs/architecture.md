# SifunaPilot Architecture

## Overview

SifunaPilot uses a modular architecture that separates concerns:

```text
User (Text/Voice/CLI)
    ↓
Command Interface
    ↓
Intent/Task Parser
    ↓
Agent Orchestrator
    ├── Planner
    ├── Model Router
    ├── Memory
    └── Permission Manager
        ↓
    Tool Registry
        ├── Browser
        ├── Desktop
        ├── Terminal
        └── Files
```

## Core Components

- **CLI**: Typer-based command interface
- **Agent**: Orchestrates task planning and execution
- **AI**: Provider-agnostic model abstraction
- **Tools**: Modular tool implementations
- **Permissions**: Security and access control
- **Config**: Pydantic-based configuration
