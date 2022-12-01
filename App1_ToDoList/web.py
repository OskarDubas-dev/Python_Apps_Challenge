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

for todo in todos:
    st.checkbox(todo)

st.text_input(key="new_todo", label="", placeholder=label, on_change=add_todo)
