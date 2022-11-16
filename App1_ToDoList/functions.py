FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return list of items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(arg, filepath=FILEPATH):
    """ Write to do item in to the text file """
    with open(filepath, 'w') as file:
        file.writelines(arg)
