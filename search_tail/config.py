class Config:  # pylint: disable=too-few-public-methods
    """Search Tail - Configuration class"""

    # Predefined keywords and their colors
    # Feel free to add more as you like.
    # Please refer to https://en.wikipedia.org/wiki/ANSI_escape_code#Colors for more options.
    keywords = {
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[91m",  # Red
        "FATAL": "\033[91m",  # Red
        "EXCEPTION": "\033[91m",  # Red
        "WARNING": "\033[93m",  # Yellow
        "WARN": "\033[93m",  # Yellow
        "NOTICE": "\033[93m",  # Yellow
        "INFO": "\033[94m",  # Blue
        "DEBUG": "\033[95m",  # Purple
        "TRACE": "\033[95m",  # Purple
        "SUCCESS": "\033[92m",  # Green
        "INPUT": "\033[96m",  # Cyan
        "OUTPUT": "\033[96m",  # Cyan
        "TODO": "\033[96m",  # Cyan
    }

    RESET_COLOR = "\033[0m"
    BOLD_FORMAT = "\033[1m"
    HIGHLIGHT_COLOR = "\033[32m"
    BACKGROUND_COLOR = "\033[100m"  # Darker grey background for current line
