# SifunaPilot

**Your computer. Your commands. Your AI.**

SifunaPilot is a local-first AI computer operator that allows a user to control their computer using natural-language text and voice.

## What is SifunaPilot?

SifunaPilot interprets natural language requests, creates execution plans, selects appropriate tools, executes actions, observes results, and reports what happened - all while maintaining strong security boundaries.

## Features

- **Natural Language Control**: Control your computer through text commands
- **Modular Architecture**: Separates AI reasoning, tool execution, and computer control
- **Local-First**: Works with local AI models (Ollama) without requiring paid APIs
- **Lightweight Models**: Optimized for 8GB RAM laptops (default: llama3.2:3b)
- **Browser Automation**: Powered by Playwright for reliable browser control
- **Security-Focused**: Permission system, confirmations, and untrusted content handling
- **Extensible**: Plugin/tool architecture for custom capabilities
- **Cross-Platform**: Support for Linux, Windows, and macOS

## Installation

### Using pipx (recommended)

```bash
pipx install sifunapilot
```

### From source

```bash
git clone https://github.com/aasz253/sifunapilot.git
cd sifunapilot
pip install -e .
```

## AI Models (Ollama)

SifunaPilot is optimized for 8GB RAM systems. Recommended lightweight models:

| Model | Size | RAM Usage | Best For |
|---|------|-----------|----------|
| `llama3.2:3b` (default) | ~2.0GB | ~3-4GB | General tasks, fast |
| `llama3.2:1b` | ~0.8GB | ~1-2GB | Very fast, minimal resources |
| `qwen2.5:3b` | ~2.0GB | ~3-4GB | Excellent reasoning |
| `smollm2:3b` | ~1.8GB | ~2-3GB | Efficient |
| `phi3.5:3.8b` | ~2.2GB | ~3-4GB | Instruction following |

Install a model with Ollama:

```bash
ollama pull llama3.2:3b
```

## Quick Start

### Check system health

```bash
sifunapilot doctor
```

### Start interactive mode

```bash
sifunapilot start
```

Then type commands:

```text
You > Open Chrome
You > Go to Google
You > Search for SifunaCodex
You > Close the tab
```

### Execute a single task

```bash
sifunapilot ask "Open Chrome and search for Python jobs"
```

## CLI Commands

```bash
sifunapilot start              # Start interactive mode
sifunapilot start --voice      # Start with voice mode
sifunapilot ask <query>        # Execute single task
sifunapilot status             # Show status
sifunapilot doctor             # Run health checks
sifunapilot providers          # List AI providers
sifunapilot tools              # List available tools
sifunapilot permissions        # Show permissions
sifunapilot config             # Show configuration
sifunapilot stop               # Stop SifunaPilot
```

## Security

SifunaPilot implements multiple security layers:
- Permission-based tool execution
- Confirmation for sensitive actions
- Web content treated as untrusted input
- No credential exposure to AI models
- Audit logging
- Dangerous command blocking

See [SECURITY.md](SECURITY.md) for details.

## Configuration

Configuration is stored in `~/.config/sifunapilot/config.yaml`. See [configuration.md](docs/configuration.md) for details.

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
mypy src/
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Status

Current version: v0.1.0 (Alpha) - Phase 1 Implementation
