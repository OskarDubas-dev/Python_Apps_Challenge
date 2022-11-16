import functions
import PySimpleGUI as sg

add_button = sg.Button("Add")
quit_button = sg.Button("Quit")

layout = \
    [
        [sg.Text("ToDo:",key="-OUTPUT-"), sg.InputText(tooltip="Enter ToDo", key="-INPUT-"), add_button],
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
    print(event, values)
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

window.close()
