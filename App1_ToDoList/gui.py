import sys

import functions
import PySimpleGUI as sg
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return "icons/" + filename


def delete_confirm(task):
    """ Create popup window to confirm removing item from the list"""
    task = task.strip("\n")
    popup_layout = [
        [sg.Text("Do you want to mark task"),
         sg.Text(text_color="Black", text=task),
         sg.Text("as completed (it will be removed from the list)?")],
        [sg.Push(), sg.Button('Yes'), sg.Button('No')]
    ]
    temp_window = sg.Window('POPUP', popup_layout, modal=True).read(close=True)
    return temp_window


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Kayak")

add_button = sg.Button(image_source=get_path("add.png"), image_subsample=20, key="-ADD-", tooltip="Add",
                       bind_return_key=True)
quit_button = sg.Button(button_text="Quit", key="-QUIT-", tooltip="Quit")
edit_button = sg.Button(image_source=get_path("edit-button.png"), image_subsample=20, key="-EDIT-",
                        tooltip="Edit")
delete_button = sg.Button(image_source=get_path("checked.png"), image_subsample=20, key="-COMPLETE-",
                          tooltip="Complete")

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
window = sg.Window("ToDo App", layout, finalize=True)
# window["-INPUT-"].bind("<Return>", "_Enter")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "-QUIT-":
        break

    match event:
        case "-ADD-":
            todos = functions.get_todos()
            newTODO = values["-INPUT-"] + "\n"
            todos.append(newTODO)
            functions.write_todos(todos)
            window["-ITEMS-"].update(values=todos)
        case "-ITEMS-":
            todo_selected = values["-ITEMS-"][0]
            window["-INPUT-"].update(value=todo_selected)
        case "-EDIT-":
            try:
                todo_to_edit = values["-ITEMS-"][0]
                new_todo = values["-INPUT-"] + "\n"
                todos = functions.get_todos()
                todos[todos.index(todo_to_edit)] = new_todo
                functions.write_todos(todos)
                window["-ITEMS-"].update(values=todos)
            except IndexError:
                sg.popup("Please select item to edit.")

        case "-COMPLETE-":
            try:
                todo_to_complete = values["-ITEMS-"][0]
                todos = functions.get_todos()
                confirm = delete_confirm(task=todo_to_complete)[0]
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
