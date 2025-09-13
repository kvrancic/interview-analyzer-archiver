import yaml
from typing import Dict, List, Any
from crewai import Task
from crewai import Agent


def load_task_config(config_path: str = "config/tasks.yaml") -> Dict[str, Any]:
    """Load task configuration from YAML file."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def create_tasks(agents: Dict[str, Agent], inputs: Dict[str, Any], config_path: str = "config/tasks.yaml") -> List[Task]:
    """
    Create all tasks from configuration file.

    Args:
        agents: Dictionary of agent_name -> Agent instance
        inputs: Input parameters for tasks (audio_path, company, role, etc.)
        config_path: Path to the tasks YAML configuration file

    Returns:
        List of Task instances in execution order
    """
    # Load configuration
    tasks_config = load_task_config(config_path)

    tasks = {}
    task_order = []

    for task_name, config in tasks_config.items():
        # Get the agent for this task
        agent_name = config['agent']
        if agent_name not in agents:
            raise ValueError(f"Agent '{agent_name}' not found for task '{task_name}'")

        agent = agents[agent_name]

        # Format description and expected output with inputs
        description = config['description'].format(**inputs)
        expected_output = config['expected_output']

        # Create the task
        task = Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

        tasks[task_name] = task
        task_order.append(task)
        print(f"Created task: {task_name}")

    # Set up task dependencies (context)
    for task_name, config in tasks_config.items():
        if 'context_from' in config:
            current_task = tasks[task_name]
            context_tasks = [tasks[dep_name] for dep_name in config['context_from'] if dep_name in tasks]
            if context_tasks:
                current_task.context = context_tasks

    return task_order