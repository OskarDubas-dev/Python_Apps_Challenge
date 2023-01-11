import streamlit as st
import pandas

st.set_page_config(layout="wide")
persian_green = "#00a7a2"
piction_blue = "#46cae4"
ship_gray = "#3a393f"
sulu = "#abed5d"

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Oskar Dubas")
    content = """
    Hello! I am Oskar. I am a programmer and a designer. My preferred programming languages are C++, Python, C# and JavaScript.
    I like working with game engines, specifically Unreal Engine, Unity and Godot. Video Game design is my passion but I also enjoy Web and Software Development.
    """

    st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
