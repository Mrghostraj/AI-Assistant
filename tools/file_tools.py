from pathlib import Path
import shutil
import os
import re 

# ============================================================
# CREATE FILE
# ============================================================

def create_file(path):
    try:
        path = Path(path)

        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

        return f"File created: {path}"

    except Exception as e:
        return f"Could not create the file: {e}"


# ============================================================
# CREATE FOLDER
# ============================================================

def create_folder(path):
    try:
        path = Path(path)

        path.mkdir(parents=True, exist_ok=True)

        return f"Folder created: {path}"

    except Exception as e:
        return f"Could not create the folder: {e}"


# ============================================================
# DELETE FILE
# ============================================================

def delete_file(path):
    try:
        path = Path(path)

        if not path.exists():
            return f"File not found: {path}"

        if not path.is_file():
            return f"This is not a file: {path}"

        path.unlink()

        return f"File deleted: {path}"

    except Exception as e:
        return f"Could not delete the file: {e}"


# ============================================================
# DELETE FOLDER
# ============================================================

def delete_folder(path):
    try:
        path = Path(path)

        if not path.exists():
            return f"Folder not found: {path}"

        if not path.is_dir():
            return f"This is not a folder: {path}"

        shutil.rmtree(path)

        return f"Folder deleted: {path}"

    except Exception as e:
        return f"Could not delete the folder: {e}"


# ============================================================
# LIST DIRECTORY
# ============================================================

def list_directory(path="."):
    try:
        path = Path(path)

        if not path.exists():
            return f"Folder not found: {path}"

        if not path.is_dir():
            return f"This is not a folder: {path}"

        items = list(path.iterdir())

        if not items:
            return "The folder is empty."

        result = []

        for item in items:

            if item.is_dir():
                result.append(f"[Folder] {item.name}")

            else:
                result.append(f"[File] {item.name}")

        return "\n".join(result)

    except Exception as e:
        return f"Could not list the folder: {e}"


# ============================================================
# CHECK EXISTS
# ============================================================

def check_path(path):
    try:
        path = Path(path)

        if not path.exists():
            return f"{path} does not exist."

        if path.is_file():
            return f"{path} is a file."

        if path.is_dir():
            return f"{path} is a folder."

    except Exception as e:
        return f"Could not check the path: {e}"


# ============================================================
# RENAME FILE / FOLDER
# ============================================================

def rename_path(old_path, new_path):
    try:
        old_path = Path(old_path)
        new_path = Path(new_path)

        if not old_path.exists():
            return f"Path not found: {old_path}"

        old_path.rename(new_path)

        return f"Renamed successfully to: {new_path}"

    except Exception as e:
        return f"Could not rename: {e}"


# ============================================================
# COPY FILE
# ============================================================

def copy_file(source, destination):
    try:
        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            return f"Source file not found: {source}"

        if not source.is_file():
            return f"Source is not a file: {source}"

        destination.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(source, destination)

        return f"File copied to: {destination}"

    except Exception as e:
        return f"Could not copy the file: {e}"


# ============================================================
# MOVE FILE / FOLDER
# ============================================================

def move_path(source, destination):
    try:
        source = Path(source)
        destination = Path(destination)

        if not source.exists():
            return f"Source not found: {source}"

        destination.parent.mkdir(parents=True, exist_ok=True)

        shutil.move(str(source), str(destination))

        return f"Moved successfully to: {destination}"

    except Exception as e:
        return f"Could not move: {e}"


# ============================================================
# OPEN FILE / FOLDER
# ============================================================

def open_path(path):
    try:
        path = Path(path)

        if not path.exists():
            return f"Path not found: {path}"

        # Windows application/file opening
        os.startfile(str(path))

        return f"Opened: {path}"

    except Exception as e:
        return f"Could not open {path}: {e}"

# ============================================================
# FILE / FOLDER TASK HANDLER
# ============================================================

def handle_file_task(text):

    text = text.lower().strip()

    # --------------------------------------------------------
    # CREATE FOLDER
    # --------------------------------------------------------

    match = re.search(
        r"(create|make|new)\s+(a\s+)?folder\s+(called|named)?\s*(.+)",
        text
    )

    if match:

        folder_name = match.group(4).strip()

        if folder_name:
            return create_folder(folder_name)


    # --------------------------------------------------------
    # CREATE FILE
    # --------------------------------------------------------

    match = re.search(
        r"(create|make|new)\s+(a\s+)?file\s+(called|named)?\s*(.+)",
        text
    )

    if match:

        file_name = match.group(4).strip()

        if file_name:
            return create_file(file_name)


    # --------------------------------------------------------
    # LIST FILES
    # --------------------------------------------------------

    if (
        "show files" in text
        or "list files" in text
        or "show folder" in text
        or "list folder" in text
        or "what files are here" in text
    ):

        return list_directory(".")


    # --------------------------------------------------------
    # CHECK FILE / FOLDER
    # --------------------------------------------------------

    match = re.search(
        r"(check|find)\s+(file|folder)\s+(.+)",
        text
    )

    if match:

        path = match.group(3).strip()

        return check_path(path)


    # --------------------------------------------------------
    # DELETE FILE
    # --------------------------------------------------------

    match = re.search(
        r"(delete|remove)\s+(file\s+)?(.+)",
        text
    )

    if match:

        path = match.group(3).strip()

        return delete_file(path)


    # --------------------------------------------------------
    # DELETE FOLDER
    # --------------------------------------------------------

    match = re.search(
        r"(delete|remove)\s+(folder|directory)\s+(.+)",
        text
    )

    if match:

        path = match.group(3).strip()

        return delete_folder(path)


    # --------------------------------------------------------
    # RENAME
    # --------------------------------------------------------

    match = re.search(
        r"rename\s+(.+?)\s+to\s+(.+)",
        text
    )

    if match:

        old_path = match.group(1).strip()
        new_path = match.group(2).strip()

        return rename_path(
            old_path,
            new_path
        )


    # --------------------------------------------------------
    # COPY
    # --------------------------------------------------------

    match = re.search(
        r"copy\s+(.+?)\s+to\s+(.+)",
        text
    )

    if match:

        source = match.group(1).strip()
        destination = match.group(2).strip()

        return copy_file(
            source,
            destination
        )


    # --------------------------------------------------------
    # MOVE
    # --------------------------------------------------------

    match = re.search(
        r"move\s+(.+?)\s+to\s+(.+)",
        text
    )

    if match:

        source = match.group(1).strip()
        destination = match.group(2).strip()

        return move_path(
            source,
            destination
        )


    # --------------------------------------------------------
    # OPEN FILE / FOLDER
    # --------------------------------------------------------

    match = re.search(
        r"(open|show)\s+(file|folder|directory)\s+(.+)",
        text
    )

    if match:

        path = match.group(3).strip()

        return open_path(path)


    # --------------------------------------------------------
    # NO FILE TASK
    # --------------------------------------------------------

    return None