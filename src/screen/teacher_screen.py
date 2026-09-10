import streamlit as st
from src.ui.base_layout import style_base_dashboard,style_base_layout
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard
def teacher_screen():
    style_base_dashboard()
    style_base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()



def teacher_screen_login():

    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut='control+backspace'):
             st.session_state['login_type']=None
             st.rerun()
    
    st.header("Login using password",text_alignment='center')

    teacher_username=st.text_input("Enter username",placeholder='Enter username')

    st.space()

    teacher_pass=st.text_input("Enter password",type="password",placeholder='Enter password')
    
    st.divider()

    btnc1,btnc2=st.columns(2)

    with btnc1:
        st.button('Login',icon=':material/passkey:',shortcut='control+enter',width='stretch')

    with btnc2:
            if st.button('Register Instead',icon=':material/passkey:',type='primary',width='stretch'):
                st.session_state.teacher_login_type='register'


    footer_dashboard()




def teacher_screen_register():

    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    
    with c2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut='control+backspace'):
            st.session_state['login_type']=None
            st.rerun()
    
    st.header("Register your Teacher profile")
    st.space()

    teacher_username=st.text_input("Enter username",placeholder='Enter username')
    teacher_name=st.text_input("Enter your name",placeholder='Enter your name')

    teacher_pass=st.text_input("Enter password",type="password",placeholder='Enter password')
    teacher_pass_confirm=st.text_input("Confirm your password",type="password",placeholder='Confirm your password')
   
    st.divider()
    
    btnc1,btnc2=st.columns(2)
    
    with btnc1:
        st.button('Register now',icon=':material/passkey:',shortcut='control+enter',width='stretch')
    
    with btnc2:
        if st.button('Login Instead',icon=':material/passkey:',type='primary',width='stretch'):
            st.session_state.teacher_login_type='login'
        
    
    footer_dashboard()
    






