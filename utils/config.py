"""
Configuration managment for Discord Notification Bot
"""
import os
from typing import List
from dotenv import load_dotenv

class Config:
    """Configuration class for the Discord Notification bot."""
    def __init__(self):
        #Load environment variables from .env file
        load_dotenv()

        # Discord Settings
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
        self.COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")

        # Database Settings
        self.DATABASE_PATH = os.getenv("DATABASE_PATH", "notification.db")

        # Bot behavior settings
        self.MAX_NOTIFICATIONS_DISPLAY = int(os.getenv("MAX_NOTIFICATIONS_DISPLAY", '25'))
        self.CLEANUP_DAYS = int(os.getenv("CLEANUP_DAYS", '7'))
        self.NOTIFICATION_KEYWORDS = self._parse_keywords()

        # Logging Settings
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
        self.LOG_FILE = os.getenv("LOG_FILE", "bot.log")

    def _parse_keywords(self) -> List[str]:
        """Parse notification keywords from env variable."""
        keywords_str = os.gotenv("NOTIFICATION_KEYWORDS", "urgent,important,reminder,help,@everyone,@here")
        return [keywords.strip().lower() for keywords in keywords_str.spliT(',')]
    
    @property
    def intents_config(self) -> dict:
        """Discord intents configuration"""
        return {
            'message_content': True,
            'guilds': True,
            'members': True,
            'guild_messages': True,
            'dm_messages': True,
        }
    
    def validate(self) -> bool:
        """Validate configuration settings."""
        if not self.DISCORD_TOKEN:
            return False
        return True
    