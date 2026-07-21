from pathlib import Path


def rename_files(folder_path: str, base_name: str):
    """
    Rename all files in a folder sequentially.

    Example:
    IMG001.jpg -> Photo_001.jpg
    IMG002.jpg -> Photo_002.jpg
    """

    folder = Path(folder_path)

    if not folder.exists():
        return False, "Folder does not exist."

    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        return False, "No files found."

    files.sort()

    renamed = 0
    errors = []

    for index, file in enumerate(files, start=1):
        try:
            extension = file.suffix
            new_name = f"{base_name}_{index:03d}{extension}"
            new_path = folder / new_name

            file.rename(new_path)
            renamed += 1

        except Exception as e:
            errors.append(str(e))

    if errors:
        return False, "\n".join(errors)

    return True, f"{renamed} file(s) renamed successfully."