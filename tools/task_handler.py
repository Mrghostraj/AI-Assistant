import re
from tools.file_tools import handle_file_task

from tools.date_time import (
    get_current_time,
    get_current_date,
    get_current_day,
    get_date_and_day,
    get_date_time
)

from tools.applications import (
    APPLICATIONS,
    open_application
)

from tools.web_tools import (
    open_google,
    open_youtube,
    google_search,
    youtube_search
)


# ============================================================
# TASK HANDLER
# ============================================================

def handle_task(text):

    text = text.lower().strip()

    print(
        f"[DEBUG] handle_task received: {text}"
    )


    # ========================================================
    # DATE + TIME
    # ========================================================

    if (
        "date and time" in text
        or "date and current time" in text
        or "day and time" in text
        or "date time" in text
    ):

        print(
            "[DEBUG] DATE + TIME TASK DETECTED"
        )

        return get_date_time()


    # ========================================================
    # CURRENT TIME
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

        print(
            "[DEBUG] TIME TASK DETECTED"
        )

        return get_current_time()


    # ========================================================
    # CURRENT DATE
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

        print(
            "[DEBUG] DATE TASK DETECTED"
        )

        return get_current_date()


    # ========================================================
    # CURRENT DAY
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

        print(
            "[DEBUG] DAY TASK DETECTED"
        )

        return get_current_day()


    # ========================================================
    # OPEN GOOGLE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+google\b",
        text
    ):

        print(
            "[DEBUG] GOOGLE TASK DETECTED"
        )

        return open_google()


    # ========================================================
    # OPEN YOUTUBE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+youtube\b",
        text
    ):

        print(
            "[DEBUG] YOUTUBE TASK DETECTED"
        )

        return open_youtube()


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    google_patterns = [

        r"search google for (.+)",
        r"search google (.+)",
        r"google search (.+)",
        r"search (.+) on google",

    ]


    for pattern in google_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            query = match.group(1).strip()

            if query:

                print(
                    "[DEBUG] GOOGLE SEARCH DETECTED"
                )

                return google_search(
                    query
                )


    # ========================================================
    # YOUTUBE SEARCH
    # ========================================================

    youtube_patterns = [

        r"search youtube for (.+)",
        r"search youtube (.+)",
        r"youtube search (.+)",
        r"search (.+) on youtube",

    ]


    for pattern in youtube_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            query = match.group(1).strip()

            if query:

                print(
                    "[DEBUG] YOUTUBE SEARCH DETECTED"
                )

                return youtube_search(
                    query
                )


    # ========================================================
    # OPEN APPLICATION
    # ========================================================

    open_patterns = [

        r"open (.+)",
        r"launch (.+)",
        r"start (.+)"

    ]


    for pattern in open_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            app_name = match.group(1).strip()

            if app_name in APPLICATIONS:

                print(
                    "[DEBUG] APPLICATION TASK DETECTED"
                )

                return open_application(
                    app_name
                )


    # ========================================================
    # NO TASK
    # ========================================================

    print(
        "[DEBUG] NO TASK DETECTED"
    )

    return None