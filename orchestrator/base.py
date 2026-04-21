"""Base classes for ValueHunter v1.0 agents."""
from __future__ import annotations

import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentModel(str, Enum):
    OPUS = "claude-opus-4-6"
    SONNET = "claude-sonnet-4-6"
    HAIKU = "claude-haiku-4-5"


class AgentLayer(int, Enum):
    GOVERNOR = 0
    SCREENING = 1
    ANALYSIS = 2
    PORTFOLIO = 3


@dataclass
class AgentResult:
    agent_id: str
    agent_name: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    tokens_used: int = 0
    duration_seconds: float = 0.0
    run_id: str = ""

    def to_dict(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "tokens_used": self.tokens_used,
            "duration_seconds": self.duration_seconds,
            "run_id": self.run_id,
        }


class BaseAgent(ABC):
    def __init__(
        self,
        agent_id: str,
        name: str,
        model: AgentModel,
        layer: AgentLayer,
        description: str = "",
        skills: list[str] | None = None,
        tools: list[str] | None = None,
        estimated_tokens: int = 5000,
    ):
        self.agent_id = agent_id
        self.name = name
        self.model = model
        self.layer = layer
        self.description = description
        self.skills = skills or []
        self.tools = tools or []
        self.estimated_tokens = estimated_tokens

    @abstractmethod
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        ...

    def info(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "model": self.model.value,
            "layer": self.layer.value,
            "description": self.description,
            "skills": self.skills,
            "tools": self.tools,
            "estimated_tokens": self.estimated_tokens,
        }
