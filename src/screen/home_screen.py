import streamlit as st

from src.components.header_home import header_home
from src.ui.base_layout import style_base_layout

def home_screen():
	st.header("Home Screen")

	header_home()

	style_base_layout()



	col1,col2=st.columns(2)

	with col1:
		if st.button("Teacher Portal",key="teacher_portal_btn"):
			st.session_state["login_type"]="teacher"
			st.rerun()
	with col2:
		if st.button("Student Portal",key="student_portal_btn"):
			st.session_state["login_type"]="student"
			st.rerun()






