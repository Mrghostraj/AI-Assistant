import re

from tools.date_time import (
    get_current_time,
    get_current_date,
    get_current_day,
    get_date_time
)

from tools.applications import (
    APPLICATIONS,
    open_application
)

from tools.web_tools import (
    open_url,
    google_search,
    youtube_search
)


def handle_task(text):

    text = text.lower().strip()

    print(f"[DEBUG] Task: {text}")


    # ========================================================
    # DATE + TIME
    # ========================================================

    if re.search(
        r"\b(date and time|date time|day and time)\b",
        text
    ):

        return get_date_time()


    # ========================================================
    # TIME
    # ========================================================

    time_patterns = [
        "what time is it",
        "what is the time",
        "tell me the time",
        "current time",
        "time right now",
        "time now",
        "what's the time"
    ]

    if any(
        pattern in text
        for pattern in time_patterns
    ):

        return get_current_time()


    # ========================================================
    # DATE
    # ========================================================

    date_patterns = [
        "what is today's date",
        "what is todays date",
        "what's today's date",
        "what date is it",
        "tell me today's date",
        "tell me todays date",
        "current date",
        "today's date",
        "todays date"
    ]

    if any(
        pattern in text
        for pattern in date_patterns
    ):

        return get_current_date()


    # ========================================================
    # DAY
    # ========================================================

    day_patterns = [
        "what day is today",
        "which day is today",
        "what is today",
        "what day is it",
        "tell me today's day"
    ]

    if any(
        pattern in text
        for pattern in day_patterns
    ):

        return get_current_day()


    # ========================================================
    # YOUTUBE ON BRAVE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+youtube\s+(on|in)\s+brave\b",
        text
    ):

        return (
            "Opening YouTube on Brave."
            if open_url(
                "https://www.youtube.com",
                "brave"
            )
            else
            "I could not open YouTube on Brave."
        )


    # ========================================================
    # OPEN GOOGLE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+google\b",
        text
    ):

        return (
            "Opening Google."
            if open_url(
                "https://www.google.com"
            )
            else
            "I could not open Google."
        )


    # ========================================================
    # OPEN YOUTUBE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+youtube\b",
        text
    ):

        return (
            "Opening YouTube."
            if open_url(
                "https://www.youtube.com"
            )
            else
            "I could not open YouTube."
        )


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    google_patterns = [
        r"search google for (.+)",
        r"search google (.+)",
        r"google search (.+)",
        r"search (.+) on google"
    ]

    for pattern in google_patterns:

        match = re.search(pattern, text)

        if match:

            query = match.group(1).strip()

            if query:
                return google_search(query)


    # ========================================================
    # YOUTUBE SEARCH
    # ========================================================

    youtube_patterns = [
        r"search youtube for (.+)",
        r"search youtube (.+)",
        r"youtube search (.+)",
        r"search (.+) on youtube"
    ]

    for pattern in youtube_patterns:

        match = re.search(pattern, text)

        if match:

            query = match.group(1).strip()

            if query:
                return youtube_search(query)


    # ========================================================
    # OPEN APPLICATION
    # ========================================================

    open_patterns = [
        r"open (.+)",
        r"launch (.+)",
        r"start (.+)"
    ]

    for pattern in open_patterns:

        match = re.search(pattern, text)

        if match:

            app_name = match.group(1).strip()

            if app_name in APPLICATIONS:

                return open_application(app_name)


    # ========================================================
    # NO TASK
    # ========================================================

    return None