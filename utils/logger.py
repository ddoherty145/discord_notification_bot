"""
Centralized logging utility for the application.
"""
import logging
import logging.handlers
from pathlib import Path
from datetime import datetime

def setup_logging(log_level: str = "INFO", log_file: str = "bot.log") -> logging.logger:
    """
    Sertup Logging configuration
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to the log file
    Returns:
        logger: Configured logger instance
    """
    # Create logs durectory if it doesn't exist
    log_path = Path(log_file)
    log_path.parent.mkdir(exist_ok=True)

    # Config root logger
    logger = logging.getLogger()
    logger.setlevel(getattr(logging, log_level.upper()))

    # Clear and existing handlers
    logger.handlers.clear()

    # Create Formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=5,  # Keep 5 backup files
    )
    file_handler.setLevel(getattr(logging, log_level.upper()))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Set discord.py logging level on WARNING to avoid spam
    logging.getLogger("discord").setLevel(logging.WARNING)
    logging.getLogger("discord.http").setLevel(logging.WARNING)

    return logger

def get_logger(name: str) -> logging.Logger:
    """
    GET a logger instance with the specified name.
    """
    return logging.getLogger(name)