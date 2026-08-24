from datetime import datetime
from zoneinfo import ZoneInfo


IST = ZoneInfo("Asia/Kolkata")


def get_current_time():
    now = datetime.now(IST)
    return now.strftime("%I:%M %p")


def get_current_date():
    now = datetime.now(IST)
    return now.strftime("%A, %d %B %Y")


# ============================================================
# TASK HANDLER
# ============================================================

def handle_task(text):

    text_lower = text.lower().strip()

    print(
        f"[DEBUG] handle_task received: {text_lower}"
    )


    # ========================================================
    # TIME TASK
    # ========================================================

    time_keywords = [
        "current time",
        "what time",
        "what's the time",
        "what is the time",
        "tell me the time",
        "time right now",
        "time now",
        "current time now"
    ]

    if any(keyword in text_lower for keyword in time_keywords):

        print("[DEBUG] TIME TASK DETECTED")

        return get_current_time()


    # ========================================================
    # DATE TASK
    # ========================================================

    date_keywords = [
        "today's date",
        "today date",
        "what is today's date",
        "what's today's date",
        "what is the date today",
        "what's the date today",
        "tell me today's date",
        "tell me the date today",
        "current date",
        "date today"
    ]

    if any(keyword in text_lower for keyword in date_keywords):

        print("[DEBUG] DATE TASK DETECTED")

        return get_current_date()


    # ========================================================
    # DAY TASK
    # ========================================================

    day_keywords = [
        "what day is today",
        "what day today",
        "which day is today",
        "which day today",
        "today's day",
        "today day",
        "tell me today's day"
    ]

    if any(keyword in text_lower for keyword in day_keywords):

        print("[DEBUG] DAY TASK DETECTED")

        return get_current_day()


    # ========================================================
    # NO TASK
    # ========================================================

    print("[DEBUG] NO TASK DETECTED")

    return None