"""
Discord Notification Bot - Main Entry Point
"""
import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from utils.config import Config
from utils.logger import setup_logging
from bot.client import NotificationBot
from database.operations import DatabaseManager

def main():
    """Main entry point for the Discord Notification Bot."""

    # Setup logging
    logger = setup_logging()

    try:
        # Load configuration
        config = Config()

        if not config.DISCORD_TOKEN:
            logger.error("Discord token is not set in the configuration.")
            logger.error("Please set the DISCORD_TOKEN in the config file.")
            return 1
        
        # Initialize database
        db_manager = DatabaseManager(config.DATABASE_PATH)
        db_manager.initialize()

        # Create bot instance
        bot = NotificationBot(config, db_manager)
        logger.info("Starting Discord Notification Bot...")

        bot.run(config.DISCORD_TOKEN)

    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
        return 0
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return 1
    
if __name__ == "__main__":
    exit(main())