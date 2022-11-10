user_prompt = "Enter a todo or \"show\" for list (type \"end\" to quit):"
todos = []

# change while exit to try/except

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





print(todos)

