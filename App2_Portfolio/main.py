import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Oskar Dubas")
    content = """
    Hello! I am Oskar. I am a programmer and a designer. My preferred programming languages are C++, Python, C# and JavaScript.
    I also like to work with game engines, specifically Unreal Engine, Unity and Godot. Video Games design is my passion but I also enjoy Web and Software Development.
    """

    st.write(content)