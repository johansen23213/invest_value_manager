"""LLM-based extraction from quarterly letter text to structured JSON."""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

import jsonschema

logger = logging.getLogger("valuehunter.spanish_funds.extractor")

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
SCHEMA_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "knowledge_base" / "schemas" / "spanish_fund_position.schema.json"
)

DEFAULT_MODEL = "claude-sonnet-4-6"


class ExtractorError(RuntimeError):
    """Raised when the LLM cannot produce schema-valid output after retry."""


class AnthropicClient(Protocol):
    """Minimal protocol matching the anthropic.Anthropic client surface we use."""
    messages: Any


def load_prompt(name: str) -> str:
    path = PROMPTS_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(str(path))
    return path.read_text()


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def _parse_response_text(msg: Any) -> str:
    """Extract the text content from an Anthropic Message object."""
    for block in msg.content:
        if getattr(block, "type", None) == "text":
            return block.text
    raise ExtractorError("no text block in LLM response")


def _call_llm(
    client: AnthropicClient,
    model: str,
    prompt: str,
    letter_text: str,
    fund_id: str,
    quarter: str,
    stricter: bool = False,
) -> str:
    user = f"fund_id: {fund_id}\nquarter hint: {quarter}\n\n--- letter text ---\n{letter_text}"
    if stricter:
        user += "\n\nPrior attempt produced malformed JSON. Return ONLY valid JSON matching the schema."
    msg = client.messages.create(
        model=model,
        max_tokens=8192,
        system=prompt,
        messages=[{"role": "user", "content": user}],
    )
    return _parse_response_text(msg)


def extract_from_text(
    letter_text: str,
    fund_id: str,
    quarter: str,
    source_url: str,
    client: AnthropicClient,
    model: str = DEFAULT_MODEL,
) -> dict:
    """Run LLM extraction + schema validation, with 1 retry on schema failure.

    Raises ExtractorError if both attempts produce invalid output.
    The caller-supplied metadata (source_url, extraction_model, extracted_at)
    is stamped onto the result, overriding whatever the LLM produced.
    """
    prompt = load_prompt("extraction_v1")
    schema = _load_schema()

    for attempt in range(2):
        raw = _call_llm(
            client, model, prompt, letter_text, fund_id, quarter,
            stricter=(attempt == 1),
        )
        try:
            result = json.loads(raw)
        except json.JSONDecodeError as e:
            logger.warning("attempt %d: invalid JSON: %s", attempt, e)
            continue
        # Stamp metadata
        result["source_url"] = source_url
        result["extraction_model"] = model
        result["extracted_at"] = datetime.now(timezone.utc).isoformat()
        result["fund_id"] = fund_id
        result["quarter"] = quarter
        # Force ticker_status=unverified to prevent LLM hallucination
        positions = result.get("positions", [])
        if isinstance(positions, list):
            for pos in positions:
                if isinstance(pos, dict):
                    pos["ticker_status"] = "unverified"
        try:
            jsonschema.validate(result, schema)
            return result
        except jsonschema.ValidationError as e:
            logger.warning("attempt %d: schema invalid: %s", attempt, e.message)
            continue

    raise ExtractorError(
        f"extraction failed for fund_id={fund_id} quarter={quarter} after 2 attempts"
    )
