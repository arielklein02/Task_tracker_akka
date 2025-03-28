from command_parser import parse_command
from task_handler import add_task, delete_task, get_tasks, mark_task, update_task


def main():
    while True:
        command_line = input('task-cli ')
        commands = parse_command(command_line)
        match commands['command']:
            case 'add':
                add_task(commands['task_name'])
            case 'delete':
                delete_task(commands['task_id'])
            case 'list':
                get_tasks(list_what=commands.get('list_what'))
            case 'mark-in-progress':
                mark_task(commands['task_id'], commands['command'])
            case 'mark-done':
                mark_task(commands['task_id'], commands['command'])
            case 'mark-todo':
                mark_task(commands['task_id'], commands['command'])
            case 'update':
                update_task(commands['task_id'], commands['task_name'])
            case _:
                print("invalid command")


if __name__ == '__main__':
    main()