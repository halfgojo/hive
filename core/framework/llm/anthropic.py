"""Anthropic Claude LLM provider - backward compatible wrapper around LiteLLM."""

import os
from collections.abc import Callable
from typing import Any

from framework.llm.litellm import LiteLLMProvider
from framework.llm.provider import LLMProvider, LLMResponse, Tool, ToolResult, ToolUse


def _get_api_key_from_credential_store() -> str | None:
    """Get API key from CredentialStoreAdapter or environment.

    Priority:
    1. CredentialStoreAdapter (supports encrypted storage + env vars)
    2. os.environ fallback
    """
    try:
        from aden_tools.credentials import CredentialStoreAdapter

        creds = CredentialStoreAdapter.default()
        if creds.is_available("anthropic"):
            return creds.get("anthropic")
    except ImportError:
        pass
    return os.environ.get("ANTHROPIC_API_KEY")


def _validate_api_key(api_key: str) -> str:
    """Validate and normalize an Anthropic API key.

    Args:
        api_key: Raw API key string

    Returns:
        Normalized API key (trimmed)

    Raises:
        ValueError: If key is malformed with specific error message
    """
    # Check for empty or whitespace-only keys
    if not api_key or not api_key.strip():
        raise ValueError(
            "Anthropic API key is empty or contains only whitespace. "
            "Check your ANTHROPIC_API_KEY environment variable or "
            "api_key parameter."
        )

    # Check for control characters BEFORE stripping (newlines, carriage returns, tabs)
    if any(char in api_key for char in '\n\r\t\x0b\x0c'):
        raise ValueError(
            "Anthropic API key contains control characters (newline, tab, etc.). "
            "This is likely a copy-paste error. Please check your key."
        )

    # Normalize: strip leading/trailing whitespace
    normalized_key = api_key.strip()

    # Check for quoted keys (common config error)
    if (normalized_key.startswith('"') and normalized_key.endswith('"')) or \
       (normalized_key.startswith("'") and normalized_key.endswith("'")):
        raise ValueError(
            "Anthropic API key appears to be quoted. "
            "Remove the surrounding quotes from your configuration."
        )

    # Check for basic Anthropic key format (starts with sk-ant-)
    if not normalized_key.startswith('sk-ant-'):
        raise ValueError(
            "Anthropic API key has unexpected format "
            f"(expected to start with 'sk-ant-'). "
            f"Received key starting with: '{normalized_key[:10]}...'"
        )

    return normalized_key


class AnthropicProvider(LLMProvider):
    """
   Anthropic Claude LLM provider.

    This is a backward-compatible wrapper that internally uses LiteLLMProvider.
    Existing code using AnthropicProvider will continue to work unchanged,
    while benefiting from LiteLLM's unified interface and features.
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "claude-haiku-4-5-20251001",
    ):
        """
        Initialize the Anthropic provider.

        Args:
            api_key: Anthropic API key. If not provided, uses CredentialStoreAdapter
                     or ANTHROPIC_API_KEY env var.
            model: Model to use (default: claude-haiku-4-5-20251001)
        """
        # Delegate to LiteLLMProvider internally.
        raw_api_key = api_key or _get_api_key_from_credential_store()
        if not raw_api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY env var or pass api_key."
            )

        # Validate and normalize the API key
        self.api_key = _validate_api_key(raw_api_key)

        self.model = model

        self._provider = LiteLLMProvider(
            model=model,
            api_key=self.api_key,
        )


    def complete(
        self,
        messages: list[dict[str, Any]],
        system: str = "",
        tools: list[Tool] | None = None,
        max_tokens: int = 1024,
        response_format: dict[str, Any] | None = None,
        json_mode: bool = False,
    ) -> LLMResponse:
        """Generate a completion from Claude (via LiteLLM)."""
        return self._provider.complete(
            messages=messages,
            system=system,
            tools=tools,
            max_tokens=max_tokens,
            response_format=response_format,
            json_mode=json_mode,
        )

    def complete_with_tools(
        self,
        messages: list[dict[str, Any]],
        system: str,
        tools: list[Tool],
        tool_executor: Callable[[ToolUse], ToolResult],
        max_iterations: int = 10,
    ) -> LLMResponse:
        """Run a tool-use loop until Claude produces a final response (via LiteLLM)."""
        return self._provider.complete_with_tools(
            messages=messages,
            system=system,
            tools=tools,
            tool_executor=tool_executor,
            max_iterations=max_iterations,
        )
