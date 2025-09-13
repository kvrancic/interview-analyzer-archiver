import os
import yaml
from typing import Dict, List, Any
from crewai import Agent
from langchain_openai import ChatOpenAI
from src.tools import TranscriptionTool, EnhancedFileWriterTool, NotionTool


def load_agent_config(config_path: str = "config/agents.yaml") -> Dict[str, Any]:
    """Load agent configuration from YAML file."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def create_tool_instance(tool_name: str):
    """Create an instance of a tool by name."""
    tool_mapping = {
        "TranscriptionTool": TranscriptionTool(),
        "EnhancedFileWriterTool": EnhancedFileWriterTool(),
        "NotionTool": NotionTool()
    }
    return tool_mapping.get(tool_name)


def create_agents(config_path: str = "config/agents.yaml") -> Dict[str, Agent]:
    """
    Create all agents from configuration file.

    Args:
        config_path: Path to the agents YAML configuration file

    Returns:
        Dictionary of agent_name -> Agent instance
    """
    # Load configuration
    agents_config = load_agent_config(config_path)

    # Get API credentials
    api_key = os.getenv('OPENROUTER_API_KEY')
    base_url = os.getenv('OPENROUTER_BASE_URL', 'https://openrouter.ai/api/v1')

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    agents = {}

    for agent_name, config in agents_config.items():
        # Create LLM instance for this agent
        # Set environment variable for OpenAI client
        os.environ['OPENAI_API_KEY'] = api_key

        # Prepend openrouter/ to model name for litellm
        model_name = f"openrouter/{config['model']}"

        llm = ChatOpenAI(
            model=model_name,
            api_key=api_key,
            base_url=base_url,
            temperature=0.7,
            default_headers={
                "HTTP-Referer": "https://github.com/yourusername/internship-agent",
                "X-Title": "Internship Assistant"
            }
        )

        # Create tool instances
        tools = []
        for tool_name in config.get('tools', []):
            tool = create_tool_instance(tool_name)
            if tool:
                tools.append(tool)

        # Create the agent
        agent = Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            llm=llm,
            tools=tools,
            verbose=config.get('verbose', True),
            allow_delegation=False
        )

        agents[agent_name] = agent
        print(f"Created agent: {agent_name}")

    return agents