import os
import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime
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
            memory=False,  # Disable memory to avoid API errors
            cache=False,  # Disable cache to avoid issues
            max_rpm=10  # Rate limiting for API calls
        )

        print("\nStarting interview analysis...")
        print("-" * 50)

        # Create output directory
        output_dir = Path(inputs.get('output_dir', 'interviews'))
        output_dir.mkdir(exist_ok=True)

        # Create a timestamped subdirectory for this analysis
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        analysis_dir = output_dir / f"analysis_{timestamp}"
        analysis_dir.mkdir(exist_ok=True)

        try:
            # Execute the crew
            result = crew.kickoff()

            # Save the final result
            final_output = analysis_dir / "final_report.md"
            with open(final_output, 'w') as f:
                f.write(str(result))
            print(f"\n✅ Final report saved to {final_output}")

            # Save metadata
            metadata = {
                "timestamp": timestamp,
                "audio_file": inputs['audio_path'],
                "company": inputs['company'],
                "role": inputs['role'],
                "status": "completed"
            }
            metadata_file = analysis_dir / "metadata.json"
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)

            print("\n" + "=" * 50)
            print("Interview analysis complete!")
            print(f"Results saved in: {analysis_dir}")
            print("=" * 50)

            return result

        except Exception as e:
            print(f"\n❌ Error during crew execution: {e}")

            # Save error log
            error_file = analysis_dir / "error_log.txt"
            with open(error_file, 'w') as f:
                f.write(f"Error occurred at: {datetime.now()}\n")
                f.write(f"Error: {str(e)}\n")

            raise