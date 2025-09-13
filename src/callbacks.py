"""
Custom callback handlers for capturing intermediary results.
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, Optional


class InterviewAnalysisCallback:
    """Callback handler to capture and save intermediary results from each agent."""

    def __init__(self, output_dir: str = "interviews"):
        """Initialize the callback handler."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Create timestamped directory for this run
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.run_dir = self.output_dir / f"run_{self.timestamp}"
        self.run_dir.mkdir(exist_ok=True)

        self.task_count = 0
        self.agent_outputs = []

    def on_task_start(self, task: Any, inputs: Dict[str, Any]) -> None:
        """Called when a task starts."""
        self.task_count += 1
        print(f"\n📋 Task {self.task_count} starting: {task.description[:50]}...")

    def on_task_complete(self, task: Any, output: Any) -> None:
        """Called when a task completes."""
        print(f"\n✅ Task {self.task_count} completed!")

        # Save the task output
        task_file = self.run_dir / f"task_{self.task_count}_output.md"
        with open(task_file, 'w') as f:
            f.write(f"# Task {self.task_count} Output\n\n")
            f.write(f"**Description:** {task.description}\n\n")
            f.write(f"**Timestamp:** {datetime.now().isoformat()}\n\n")
            f.write("## Output\n\n")
            f.write(str(output))

        print(f"   Saved to: {task_file}")

        # Keep track of outputs
        self.agent_outputs.append({
            "task_number": self.task_count,
            "description": task.description,
            "output_file": str(task_file),
            "timestamp": datetime.now().isoformat()
        })

    def on_agent_action(self, agent: Any, action: str, tool: Optional[str] = None) -> None:
        """Called when an agent takes an action."""
        if tool:
            print(f"   🔧 Agent using tool: {tool}")

    def save_summary(self) -> None:
        """Save a summary of all outputs."""
        summary_file = self.run_dir / "summary.json"
        with open(summary_file, 'w') as f:
            json.dump({
                "timestamp": self.timestamp,
                "total_tasks": self.task_count,
                "outputs": self.agent_outputs
            }, f, indent=2)

        print(f"\n📊 Summary saved to: {summary_file}")