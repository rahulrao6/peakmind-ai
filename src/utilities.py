# utilities.py
import re

def clean_text(text):
    """
    Utility function to clean text by removing non-alphanumeric characters and extra spaces.
    """
    # Remove special characters and digits
    text_cleaned = re.sub("(\\d|\\W)+", " ", text)
    return text_cleaned.strip()

def format_timestamp(timestamp):
    """
    Utility function to format timestamps for display.
    """
    from datetime import datetime
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
