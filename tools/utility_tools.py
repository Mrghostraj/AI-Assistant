from datetime import datetime


# ============================================================
# TIME
# ============================================================

TIME_KEYWORDS = [
    "what time",
    "current time",
    "tell me the time",
    "time is it",
    "time right now",
]


def get_time():
    return datetime.now().strftime("%I:%M %p")


# ============================================================
# DATE
# ============================================================

DATE_KEYWORDS = [
    "today's date",
    "todays date",
    "what is the date",
    "what's the date",
    "tell me the date",
    "date today",
    "today date",
    "what date is it",
]


def get_date():
    return datetime.now().strftime("%A, %d %B %Y")


# ============================================================
# DAY
# ============================================================

DAY_KEYWORDS = [
    "what day is it",
    "what day is today",
    "which day is it",
    "which day is today",
    "today's day",
]


def get_day():
    return datetime.now().strftime("%A")


# ============================================================
# TASK HANDLER
# ============================================================

def handle_task(text):

    text_lower = text.lower().strip()

    # Time
    if any(keyword in text_lower for keyword in TIME_KEYWORDS):
        return f"It is {get_time()}."

    # Date
    if any(keyword in text_lower for keyword in DATE_KEYWORDS):
        return f"Today is {get_date()}."

    # Day
    if any(keyword in text_lower for keyword in DAY_KEYWORDS):
        return f"Today is {get_day()}."

    return None

