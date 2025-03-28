from file_handler import get_file_info


def get_new_task_id(file_path: str | None = None) -> str:
    data = get_file_info(file_path)
    ids = []
    for key in data.keys():
        if key:
            ids.append(int(key))

    if not ids:
        ids.append(-1)

    return str(ids[-1] + 1)

