import streamlit as st
import functions

todos = functions.get_todos()
label = "Enter a Todo:"


def add_todo():
    _todo = st.session_state["new_todo"] + "\n"
    todos.append(_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My ToDo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key="checkbox_" + todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state["checkbox_"+todo]
        st._rerun()


st.text_input(key="new_todo", label="", placeholder=label, on_change=add_todo)