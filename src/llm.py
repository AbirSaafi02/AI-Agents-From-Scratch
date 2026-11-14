import json
import urllib.request
from dataclasses import dataclass


@dataclass
class Response:
    """Structured response returned by LLM calls.
    
    Normalizes outputs across different inference engines (Ollama, OpenRouter, etc.).
    Note: `reasoning` and `tool_call` are prepared here as placeholders and will be
    activated in upcoming chapters (Chapter 3 for Reasoning, Chapter 5 for Tools).
    """
    content: str = ""
    reasoning: str | None = None
    tool_call: dict | None = None
    metadata: dict | None = None


class LLM:
    """Lightweight OpenAI-compatible LLM wrapper."""

    def __init__(
        self,
        model: str = "qwen2.5:7b",
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",
        temperature: float | None = None,
    ) -> None:
        """Initialize the LLM client configuration."""
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.temperature = temperature

    def generate(
        self, messages: list[dict], tools: list | None = None
    ) -> Response:
        """Send a list of messages to the LLM and return a structured Response.
        
        Note: Native reasoning is intentionally disabled/omitted in Chapter 2
        so we can explicitly build prompt-based reasoning from scratch in Chapter 3.
        """
        # 1. Build the standard OpenAI-compatible request payload
        body: dict = {
            "model": self.model,
            "messages": messages,
        }

        if tools:
            body["tools"] = tools
        if self.temperature is not None:
            body["temperature"] = self.temperature

        # 2. Send POST request to /chat/completions
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
        )

        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read())

        # 3. Extract message content, optional reasoning/tools, and token metadata
        message = data["choices"][0]["message"]
        reasoning = message.get("reasoning") or message.get("reasoning_content")
        tool_calls = message.get("tool_calls")
        tool_call = tool_calls[0] if tool_calls else None

        usage = data.get("usage", {})
        metadata = {
            "model": data.get("model"),
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
        }

        # 4. Return normalized Response dataclass
        return Response(
            content=message.get("content", ""),
            reasoning=reasoning,
            tool_call=tool_call,
            metadata=metadata,
        )