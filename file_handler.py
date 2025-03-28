import json
import os


def get_file_info(file_path: str | None = None) -> dict:
    """
    gets json file info from file
    :param file_path: the file path to load the json from
    :return: json dict
    """
    file_path = file_path or 'tasks.json'
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            json.dump({}, file)

    with open(file_path, 'r') as file:
        return json.load(file)


def write_file_info(data: dict, file_path: str | None = None):
    """
    gets a dict and writes it all to the file at file_path
    :param data: the json data to write
    :param file_path: the file path to write to
    """
    file_path = file_path or 'tasks.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)
