from .llm import LLM
from .trajectory import Trajectory


class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self, llm: LLM) -> None:
        # Chapter 2: Plug in the Brain (LLM) and Execution Tracker (Trajectory)
        self.llm = llm
        self.trajectory = Trajectory()

        # Upcoming modules (placeholders from Chapter 1)
        self.memory = None   # Chapter 4: Add Memory
        self.tools = None    # Chapter 5: Add Tools
        self.planner = None  # Chapter 6: Add Planning

    def run(self, task: str) -> str:
        """Initialize a new trajectory run and execute the agent on a task."""
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single interaction step with the LLM.
        
        In Chapter 2, this is a direct single-turn LLM call without reasoning
        or tool loops, which will be introduced in Chapters 3, 5, and 6.
        """
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str | None:
        """Execute a tool action (placeholder for Chapter 5)."""
        return f"Executed action: {action}"