import streamlit as st

st.set_page_config(layout="wide")

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