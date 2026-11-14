from dataclasses import dataclass
from .llm import Response


@dataclass
class Step:
    """Represents a single step in an agent's execution trajectory.
    
    Designed around the THOUGHT -> ACTION -> OBSERVATION loop:
    - `thought`: Internal reasoning trace (activated in Chapter 3).
    - `action` & `observation`: Tool execution and its output (activated in Chapters 5-6).
    - `answer`: Final response returned to the user when the turn ends.
    """
    thought: str = ""
    action: dict | None = None
    observation: str | None = None
    answer: str | None = None
    metadata: dict | None = None


class Trajectory:
    """Records agent execution across multiple runs as a sequence of steps."""

    def __init__(self) -> None:
        self.runs: list[dict] = []

    def initialize(self, query: str) -> None:
        """Start tracking a new execution run for a given user query."""
        self.runs.append({"query": query, "steps": []})

    def add(self, response: Response, observation: str | None = None) -> None:
        """Record a new Step from an LLM Response.
        
        If an `observation` is provided, the step is logged as a tool interaction
        (ACTION + OBSERVATION). Otherwise, it is logged as a final ANSWER.
        """
        # Capture THOUGHT (empty in Chapter 2 since reasoning is not enabled yet) and metadata
        step = Step(
            thought=response.reasoning or "",
            metadata=response.metadata,
        )

        # Record either an intermediate tool step or the final answer
        if observation is not None:
            step.action = response.tool_call
            step.observation = observation
        else:
            step.answer = response.content

        self.runs[-1]["steps"].append(step)