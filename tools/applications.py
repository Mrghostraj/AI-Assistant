import subprocess

def open_application(app_name):

    app_name = app_name.lower().strip()

    try:

        subprocess.Popen(
            [
                "cmd.exe",
                "/c",
                "start",
                "",
                app_name
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return f"Opening {app_name}."

    except Exception as e:

        print("[ERROR] Application:", e)

        return f"I could not open {app_name}."


if __name__ == "__main__":

    print(open_application("chrome"))