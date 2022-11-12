user_prompt = "Enter a todo or \"show\" for list (type \"end\" to quit):"
todos = []

# change while exit to try/except


FILEPATH = "todos_item.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local








while True:
    status = input(user_prompt)
    status = status.strip()
    match status:
        case "end":
            break
        case "show":
            for i in todos:
                print(i)
        case default:
            todos.append(status)






#ok jump straight to desktop gui

print(todos)

