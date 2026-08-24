from datetime import datetime

def get_time():
    """Return current local time"""
    return datetime.now().strftime("%I:%M %p")

def get_date():
    """Return the current date"""
    return datetime.now().strftime("%A, %d %B %Y")

