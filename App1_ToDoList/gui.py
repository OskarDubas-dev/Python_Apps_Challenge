import functions
import PySimpleGUI as sg


def popup_confirm(task):
    """ Create popup window to confirm removing item from the list"""
    popup_layout = [
        [sg.Text("Do you want to mark task "),
         sg.Text(text_color="Black", text=task),
         sg.Text(" as completed (it will be removed from the list)?")],
        [sg.Push(), sg.Button('Yes'), sg.Button('No')]
    ]
    temp_window = sg.Window('POPUP', popup_layout, modal=True).read(close=True)
    return temp_window


add_button = sg.Button("Add")
quit_button = sg.Button("Quit")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Complete")

tooltip_text = "Enter ToDo"

list_box = sg.Listbox(values=functions.get_todos(), key="-ITEMS-",
                      enable_events=True, size=[60, 20])

layout = \
    [
        [sg.Text(tooltip_text, key="-OUTPUT-"), sg.InputText(tooltip=tooltip_text, key="-INPUT-"), add_button],
        [list_box, edit_button, delete_button],
        [quit_button]
    ]

# create window
window = sg.Window("ToDo App", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    match event:
        case "Add":
            todos = functions.get_todos()
            newTODO = values["-INPUT-"] + "\n"
            todos.append(newTODO)
            functions.write_todos(todos)
            window["-ITEMS-"].update(values=todos)
        case "-ITEMS-":
            todo_selected = values["-ITEMS-"][0]
            window["-INPUT-"].update(value=todo_selected)
        case "Edit":
            try:
                todo_to_edit = values["-ITEMS-"][0]
                new_todo = values["-INPUT-"] + "\n"
                todos = functions.get_todos()
                todos[todos.index(todo_to_edit)] = new_todo
                window["-ITEMS-"].update(values=todos)
            except IndexError:
                sg.popup("Please select item to edit.")

        case "Complete":
            try:
                todo_to_complete = values["-ITEMS-"][0]
                todos = functions.get_todos()
                confirm = popup_confirm(task=todo_to_complete)[0]
                print(confirm)
                if confirm == "Yes":
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos)
                    window["-ITEMS-"].update(values=todos)
                    window["-INPUT-"].update(value="")
            except IndexError:
                sg.popup("Please select item to complete.")


    print(event, values)
    window.refresh()

window.close()
