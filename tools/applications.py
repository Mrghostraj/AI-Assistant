import subprocess


# ============================================================
# APPLICATION COMMANDS
# ============================================================

APPLICATIONS = {

    "chrome": "start chrome",
    "google chrome": "start chrome",

    "brave": "start brave",
    "brave browser": "start brave",

    "calculator": "start calc",

    "notepad": "start notepad",

    "file explorer": "start explorer",
    "explorer": "start explorer",

    "command prompt": "start cmd",
    "cmd": "start cmd",

}


# ============================================================
# OPEN APPLICATION
# ============================================================

def open_application(app_name):

    app_name = app_name.lower().strip()

    command = APPLICATIONS.get(app_name)

    if command is None:

        return f"I don't know how to open {app_name}."


    try:

        subprocess.Popen(
            [
                "cmd.exe",
                "/c",
                command
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return f"Opening {app_name}."


    except Exception as e:

        print("[ERROR] Application:", e)

        return f"I could not open {app_name}."


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print(open_application("calculator"))