def parse_command(command_line: str) -> dict[str, str]:
    """
    a simple command parses that returns a dict with known keys
    :param command_line: the command line from the user
    :return: a dict with known keys
    """
    tokens = command_line.split('"')
    opcode = tokens[0].split(' ')
    commands = {'command': opcode[0]}

    try:
        if opcode[1]:
            if opcode[1].isnumeric():
                commands['task_id'] = opcode[1]
            else:
                commands['list_what'] = opcode[1]
    except IndexError:
        pass

    try:
        if tokens[1]:
            commands['task_name'] = tokens[1]

    except IndexError:
        pass

    return commands
