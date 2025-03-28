from file_handler import get_file_info, write_file_info
from datetime import datetime

from utils import get_new_task_id


def add_task(name: str, file_path: str | None = None):
    """
    create a new task and add it to the json file
    :param name: the name of the task
    :param file_path: the file path to write to
    """
    data = get_file_info(file_path)

    data[get_new_task_id(file_path)] = {
        'name': name,
        'status': 'todo',
        'created_at': str(datetime.now()),
        'last_updated_at': str(datetime.now()),
    }

    write_file_info(data, file_path)


def delete_task(task_id: str, file_path: str | None = None):
    """
    deletes a task by task_id
    :param task_id: the task id to delete
    :param file_path: the file path to delete from
    """
    data = get_file_info(file_path)
    try:
        del data[task_id]
    except KeyError:
        print(f'error: task id {task_id} not found.')
        return

    write_file_info(data, file_path)


def get_tasks(list_what: str | None = None, file_path: str | None = None):
    """
    prints all the tasks by a certain status (or all)
    :param list_what: 'todo', 'in-progress' or 'done'
    :param file_path: the file path to read from
    """
    data = get_file_info(file_path)
    if not list_what:
        for task in data.keys():
            print(f'{task} - {data[task]["name"]} - {data[task]["status"]} - created at: {data[task]['created_at']} -'
                  f' last updated at: {data[task]['last_updated_at']}')
    if list_what == 'in-progress':
        for task in data.keys():
            if data[task]['status'] == 'in-progress':
                print(
                    f'{task} - {data[task]["name"]} - {data[task]["status"]} - created at: {data[task]['created_at']} -'
                    f' last updated at: {data[task]['last_updated_at']}')
    elif list_what == 'done':
        for task in data.keys():
            if data[task]['status'] == 'done':
                print(
                    f'{task} - {data[task]["name"]} - {data[task]["status"]} - created at: {data[task]['created_at']} -'
                    f' last updated at: {data[task]['last_updated_at']}')
    elif list_what == 'todo':
        for task in data.keys():
            if data[task]['status'] == 'todo':
                print(
                    f'{task} - {data[task]["name"]} - {data[task]["status"]} - created at: {data[task]['created_at']} -'
                    f' last updated at: {data[task]['last_updated_at']}')


def mark_task(task_id: str, mark: str, file_path: str | None = None):
    """
    mark a task a certain status
    :param task_id: the task id to mark
    :param mark: the mark
    :param file_path: the file to read and write from
    """
    data = get_file_info(file_path)
    try:
        data[task_id]['status'] = mark[5::]
        data[task_id]['last_updated_at'] = str(datetime.now())
    except KeyError:
        print(f'error: task id {task_id} not found.')

    write_file_info(data, file_path)


def update_task(task_id: str, new_name: str, file_path: str | None = None):
    """
    update the name of a task
    :param task_id: the task id to update
    :param new_name: the new name of the task
    :param file_path: the file path to read and write from
    """
    data = get_file_info(file_path)
    try:
        data[task_id]['name'] = new_name
        data[task_id]['last_updated_at'] = str(datetime.now())
    except KeyError:
        print(f'error: task id {task_id} not found.')

    write_file_info(data, file_path)
