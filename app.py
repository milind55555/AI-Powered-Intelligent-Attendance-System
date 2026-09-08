import streamlit as st
from src.screen.teacher_screen import  teacher_screen
from src.screen.student_screen import  student_screen
from  src.screen.home_screen import home_screen

def main():
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None


    if  st.session_state["login_type"] == "teacher":
        teacher_screen()

    elif  st.session_state["login_type"] =="student":
        student_screen()

    else :
        home_screen()    
main()   