"""Telegram notification sender for ValueHunter digest messages."""
from __future__ import annotations
import logging
import os
from typing import Any

logger = logging.getLogger("valuehunter.notifications")

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

class TelegramNotifier:
    def __init__(self, bot_token: str = "", chat_id: str = ""):
        self.bot_token = bot_token or TELEGRAM_BOT_TOKEN
        self.chat_id = chat_id or TELEGRAM_CHAT_ID

    @property
    def is_configured(self) -> bool:
        return bool(self.bot_token and self.chat_id)

    async def send(self, message: str) -> bool:
        if not self.is_configured:
            logger.warning("Telegram not configured (missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID)")
            return False
        try:
            import httpx
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            # Split long messages (Telegram 4096 char limit)
            chunks = [message[i:i+4000] for i in range(0, len(message), 4000)]
            async with httpx.AsyncClient() as client:
                for chunk in chunks:
                    resp = await client.post(url, json={
                        "chat_id": self.chat_id,
                        "text": chunk,
                        "parse_mode": "Markdown",
                    })
                    if resp.status_code != 200:
                        logger.error(f"Telegram API error: {resp.status_code} {resp.text}")
                        return False
            return True
        except Exception as e:
            logger.error(f"Telegram send failed: {e}")
            return False

    async def send_weekly_digest(self, result: dict[str, Any]) -> bool:
        from notifications.formatters import format_weekly_digest
        return await self.send(format_weekly_digest(result))

    async def send_daily_digest(self, result: dict[str, Any]) -> bool:
        from notifications.formatters import format_daily_digest
        return await self.send(format_daily_digest(result))

    async def send_on_demand(self, result: dict[str, Any]) -> bool:
        from notifications.formatters import format_on_demand
        return await self.send(format_on_demand(result))
