# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CrewAI-based project for building an "Automated Internship Assistant" - a multi-agent system that processes interview audio recordings and provides structured feedback through Notion integration.

## Development Commands

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies (once requirements.txt exists)
pip install -r requirements.txt
```

### Running the Application
```bash
# Main execution (once implemented)
python src/main.py

# Run specific crew (expected pattern)
python src/crew.py
```

### Testing
```bash
# Run tests (once test framework is set up)
pytest tests/

# Run specific test file
pytest tests/test_agents.py
```

## Architecture

### Multi-Agent System Design
The system implements a 6-agent sequential workflow:

1. **Transcriptionist Agent**: Converts audio to text using AssemblyAI/Deepgram/Whisper
2. **Dialogue Structurer Agent**: Parses Q&A format from transcription
3. **Technical Solution Architect Agent**: Evaluates technical responses using qwen3-next-80b-a3b-thinking model
4. **Performance Analyst & Coach Agent**: Provides holistic performance review
5. **Quality Assurance Editor Agent**: Final review and editing
6. **Notion Exporter Agent**: Saves to Notion database via MCP server

### Key External Integrations
- **OpenRouter API**: Model access (requires OPENROUTER_API_KEY)
- **Notion MCP Server**: Database integration (requires notion-mcp-server setup)

### Model Configuration
- Default model: `google/gemini-2.5-flash-lite` for most agents
- Technical analysis: `qwen/qwen3-next-80b-a3b-thinking` for deep reasoning

## Project Structure (Expected)
```
src/
├── agents/           # Agent definitions with roles and goals
├── tasks/            # Task definitions and expected outputs
├── tools/            # Custom tools and integrations
├── interviews/       # Output interviews when notion key is not available
├── crew.py           # Main crew orchestration
└── main.py           # Entry point

config/
├── agents.yaml       # Agent configurations (if using YAML)
└── tasks.yaml        # Task configurations (if using YAML)
```

## Important Implementation Notes

- Each agent requires: role, goal, backstory, tools list
- Each task requires: description, agent assignment, expected_output
- Tasks execute sequentially with context passing between them
- Terminal interaction is required per assignment specs
- Audio files are expected in a designated input directory
- if Notion key is not available, you can output in the custom .md file in the root of the project - make skeleton for it. 

## API Keys Required
- OPENROUTER_API_KEY
- Notion integration credentials (for MCP server)