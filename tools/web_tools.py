import subprocess
import urllib.parse


# ============================================================
# OPEN URL
# ============================================================

def open_url(url):

    try:

        subprocess.Popen(
            [
                "cmd.exe",
                "/c",
                "start",
                "",
                url
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return True


    except Exception as e:

        print("[ERROR] Browser:", e)

        return False


# ============================================================
# OPEN GOOGLE
# ============================================================

def open_google():

    success = open_url(
        "https://www.google.com"
    )

    if success:
        return "Opening Google."

    return "I could not open Google."


# ============================================================
# OPEN YOUTUBE
# ============================================================

def open_youtube():

    success = open_url(
        "https://www.youtube.com"
    )

    if success:
        return "Opening YouTube."

    return "I could not open YouTube."


# ============================================================
# GOOGLE SEARCH
# ============================================================

def google_search(query):

    query = query.strip()

    if not query:

        return "What would you like me to search for?"


    encoded_query = urllib.parse.quote_plus(
        query
    )

    url = (
        "https://www.google.com/search?q="
        + encoded_query
    )


    success = open_url(url)

    if success:

        return f"Searching Google for {query}."

    return "I could not perform the Google search."


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(query):

    query = query.strip()

    if not query:

        return "What would you like me to search for on YouTube?"


    encoded_query = urllib.parse.quote_plus(
        query
    )

    url = (
        "https://www.youtube.com/results?search_query="
        + encoded_query
    )


    success = open_url(url)

    if success:

        return f"Searching YouTube for {query}."

    return "I could not perform the YouTube search."


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print(open_google())

    # Uncomment when testing:
    # print(open_youtube())
    # print(google_search("Python machine learning"))
    # print(youtube_search("Python tutorial"))