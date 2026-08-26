import subprocess
import urllib.parse

def open_url(url, browser=None):

    try:

        if browser:

            command = [
                "cmd.exe",
                "/c",
                "start",
                "",
                browser,
                url
            ]

        else:

            command = [
                "cmd.exe",
                "/c",
                "start",
                "",
                url
            ]

        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return True

    except Exception as e:

        print("[ERROR] Browser:", e)

        return False


def open_website(name, url):

    if open_url(url):
        return f"Opening {name}."

    return f"I could not open {name}."


def google_search(query):

    query = query.strip()

    if not query:
        return "What would you like me to search for?"

    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote_plus(query)
    )

    if open_url(url):
        return f"Searching Google for {query}."

    return "I could not perform the Google search."


def youtube_search(query):

    query = query.strip()

    if not query:
        return "What would you like me to search for on YouTube?"

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote_plus(query)
    )

    if open_url(url):
        return f"Searching YouTube for {query}."

    return "I could not perform the YouTube search."


if __name__ == "__main__":

    # print(open_website(
    #     "Google",
    #     "https://www.google.com"
    # ))

    # print(open_website(
    #     "YouTube",
    #     "https://www.youtube.com"
    # ))

    # print(google_search("Python machine learning"))

    print(youtube_search("Python tutorial"))