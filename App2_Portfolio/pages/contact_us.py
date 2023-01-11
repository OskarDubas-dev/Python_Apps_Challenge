import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        send_email(email=user_email, message=message)
        st.info("Your email has been sent successfully")
