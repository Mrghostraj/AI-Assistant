import subprocess
import re
import urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo


# ============================================================
# DATE / TIME
# ============================================================

def get_current_time():
    india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    return india_time.strftime(
        "It is %I:%M %p."
    )


def get_current_date():
    india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

    return india_time.strftime(
        "Today is %A, %d %B %Y."
    )


# ============================================================
# OPEN APPLICATIONS
# ============================================================

APPLICATIONS = {

    "chrome": "start chrome",
    "google chrome": "start chrome",

    "calculator": "start calc",

    "notepad": "start notepad",

    "file explorer": "start explorer",
    "explorer": "start explorer",

    "command prompt": "start cmd",
    "cmd": "start cmd",

}


def open_application(app_name):

    app_name = app_name.lower().strip()

    command = APPLICATIONS.get(app_name)

    if not command:
        return None

    try:

        subprocess.Popen(
            ["cmd.exe", "/c", command],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return f"Opening {app_name}."

    except Exception as e:

        print("[ERROR] Application:", e)

        return f"I could not open {app_name}."


# ============================================================
# BROWSER
# ============================================================

def open_url(url):

    try:

        subprocess.Popen(
            ["cmd.exe", "/c", "start", "", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return True

    except Exception as e:

        print("[ERROR] Browser:", e)

        return False


def open_google():

    if open_url("https://www.google.com"):
        return "Opening Google."

    return "I could not open Google."


def open_youtube():

    if open_url("https://www.youtube.com"):
        return "Opening YouTube."

    return "I could not open YouTube."


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(query):

    query = query.strip()

    if not query:
        return "What would you like me to search for?"

    encoded_query = urllib.parse.quote_plus(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    if open_url(url):

        return f"Searching Google for {query}."

    return "I could not perform the Google search."


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(query):

    query = query.strip()

    if not query:
        return "What would you like me to search for on YouTube?"

    encoded_query = urllib.parse.quote_plus(query)

    url = f"https://www.youtube.com/results?search_query={encoded_query}"

    if open_url(url):

        return f"Searching YouTube for {query}."

    return "I could not perform the YouTube search."


# ============================================================
# TASK HANDLER
# ============================================================

def handle_task(text):

    text = text.lower().strip()

    print(f"[DEBUG] handle_task received: {text}")

    # ========================================================
    # TIME
    # ========================================================

    time_keywords = [
        "current time",
        "what time is it",
        "tell me the time",
        "time now",
        "time"
    ]

    if any(keyword in text for keyword in time_keywords):

        print("[DEBUG] TIME TASK DETECTED")

        return get_current_time()


    # ========================================================
    # DATE
    # ========================================================

    date_keywords = [
        "today's date",
        "todays date",
        "what date is it",
        "what is the date",
        "tell me the date",
        "current date",
        "today date",
        "which day is today",
        "what day is today"
    ]

    if any(keyword in text for keyword in date_keywords):

        print("[DEBUG] DATE TASK DETECTED")

        return get_current_date()


    # ========================================================
    # OPEN GOOGLE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+(google)\b",
        text
    ):

        print("[DEBUG] GOOGLE TASK DETECTED")

        return open_google()


    # ========================================================
    # OPEN YOUTUBE
    # ========================================================

    if re.search(
        r"\b(open|launch|start)\s+(youtube)\b",
        text
    ):

        print("[DEBUG] YOUTUBE TASK DETECTED")

        return open_youtube()


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    google_patterns = [

        r"search google for (.+)",
        r"search google (.+)",
        r"google search (.+)",
        r"search for (.+)",
        r"search (.+) on google",

    ]

    for pattern in google_patterns:

        match = re.search(pattern, text)

        if match:

            query = match.group(1).strip()

            # Avoid treating generic "search" as a query
            if query:

                print("[DEBUG] GOOGLE SEARCH DETECTED")

                return google_search(query)


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

        match = re.search(pattern, text)

        if match:

            query = match.group(1).strip()

            if query:

                print("[DEBUG] YOUTUBE SEARCH DETECTED")

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

            # Don't accidentally handle websites here
            if app_name in APPLICATIONS:

                print("[DEBUG] APPLICATION TASK DETECTED")

                return open_application(app_name)


    # ========================================================
    # NO TASK
    # ========================================================

    print("[DEBUG] NO TASK DETECTED")

    return None