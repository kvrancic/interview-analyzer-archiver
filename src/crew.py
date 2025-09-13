import os
from typing import Dict, Any
from dotenv import load_dotenv
from crewai import Crew, Process
from src.agents import create_agents
from src.tasks import create_tasks


class InterviewAssistantCrew:
    """Main crew orchestration for the Interview Assistant."""

    def __init__(self):
        """Initialize the Interview Assistant Crew."""
        # Load environment variables
        load_dotenv()

        # Verify API key is available
        if not os.getenv('OPENROUTER_API_KEY'):
            raise ValueError(
                "OPENROUTER_API_KEY not found in environment variables. "
                "Please create a .env file with your OpenRouter API key."
            )

        # Create agents and store them
        print("Initializing Interview Assistant Crew...")
        print("-" * 50)
        self.agents = create_agents()

    def kickoff(self, inputs: Dict[str, Any]) -> str:
        """
        Execute the interview analysis workflow.

        Args:
            inputs: Dictionary containing:
                - audio_path: Path to the audio file
                - company: Company name (optional)
                - role: Role applied for (optional)

        Returns:
            Final analysis result as a string
        """
        # Validate inputs
        if 'audio_path' not in inputs:
            raise ValueError("audio_path is required in inputs")

        # Set defaults for optional inputs
        inputs.setdefault('company', 'Unknown Company')
        inputs.setdefault('role', 'Unknown Role')

        # Create tasks with the current inputs
        print("\nCreating tasks...")
        print("-" * 50)
        tasks = create_tasks(self.agents, inputs)

        # Create and configure the crew
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=tasks,
            process=Process.sequential,  # Tasks execute in order
            verbose=True,  # Show detailed execution logs
            memory=True,  # Enable memory for better context
            cache=True,  # Cache results for efficiency
            max_rpm=10  # Rate limiting for API calls
        )

        print("\nStarting interview analysis...")
        print("-" * 50)

        # Execute the crew
        result = crew.kickoff()

        print("\n" + "=" * 50)
        print("Interview analysis complete!")
        print("=" * 50)

        return result