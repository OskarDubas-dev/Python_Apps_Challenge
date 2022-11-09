
user_prompt = "Enter a todo (type \"end\" to quit):"
status = ""
todos = []

#change while exit to try/except

while status != "end":
    status = input(user_prompt)
    if status != "end" and status != "":
        todos.append(status)


for todo in todos:
    print(todo)
