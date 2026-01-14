"""Telegram Tool for sending formatted alerts to group"""
import os
import requests
from typing import Any
from crewai.tools import BaseTool
from pydantic import Field


class TelegramNotificationTool(BaseTool):
    """Tool for sending formatted notifications to Telegram group"""

    name: str = "Telegram Alert Sender"
    description: str = (
        "Sends formatted lead alert messages to the configured Telegram group. "
        "Accepts markdown formatted text with alert details."
    )

    bot_token: str = Field(default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN", ""))
    group_id: str = Field(default_factory=lambda: os.getenv("TELEGRAM_GROUP_ID", ""))
    thread_id: str = Field(default_factory=lambda: os.getenv("TELEGRAM_THREAD_ID", ""))

    def _run(self, message: str) -> str:
        """
        Send a message to the configured Telegram group

        Args:
            message: Formatted message text (supports Markdown)

        Returns:
            Success or error message
        """
        if not self.bot_token or not self.group_id:
            raise ValueError("TELEGRAM_BOT_TOKEN and TELEGRAM_GROUP_ID must be set in environment")

        try:
            # Use Telegram Bot API directly
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

            payload = {
                "chat_id": self.group_id,
                "text": message,
                "parse_mode": "HTML",
                "disable_web_page_preview": True
            }

            # Add thread_id if sending to a topic/subtopic
            if self.thread_id:
                payload["message_thread_id"] = int(self.thread_id)

            response = requests.post(url, json=payload, timeout=10)

            if response.status_code == 200:
                return f"✅ Message sent successfully to Telegram group {self.group_id}"
            else:
                error_data = response.json()
                error_msg = error_data.get("description", "Unknown error")
                return f"❌ Telegram API error: {error_msg}"

        except requests.exceptions.Timeout:
            return "❌ Error: Request to Telegram API timed out"
        except requests.exceptions.RequestException as e:
            return f"❌ Network error sending Telegram message: {str(e)}"
        except Exception as e:
            return f"❌ Error sending Telegram message: {str(e)}"
