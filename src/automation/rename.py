from pathlib import Path


def generate_preview(folder_path: str, base_name: str):
    """
    Generate old and new filenames without renaming files.
    """

    folder = Path(folder_path)

    if not folder.exists():
        return False, "Folder does not exist."

    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        return False, "No files found."

    files.sort()

    preview = []

    for index, file in enumerate(files, start=1):
        extension = file.suffix
        new_name = f"{base_name}_{index:03d}{extension}"

        preview.append(
            {
                "old_name": file.name,
                "new_name": new_name,
                "path": file,
            }
        )

    return True, preview


def rename_files(preview):
    """
    Rename files using the generated preview.
    """

    renamed = 0
    errors = []

    for item in preview:
        try:
            old_path = item["path"]
            new_path = old_path.parent / item["new_name"]

            old_path.rename(new_path)
            renamed += 1

        except Exception as e:
            errors.append(str(e))

    if errors:
        return False, "\n".join(errors)

    return True, f"{renamed} file(s) renamed successfully."