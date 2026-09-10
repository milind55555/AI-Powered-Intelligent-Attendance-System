import streamlit as st
from src.ui.base_layout import style_base_dashboard,style_base_layout
from src.components.header_home import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists,create_teacher,teacher_login


def teacher_screen():
    style_base_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data=st.session_state.teacher_data

    st.header(f"""Welcome,{teacher_data['name']}""")

def login_teacher(username,password):
    if not username or not password:
        return False

    teacher=teacher_login(username,password)

    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True
    return False

        

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
        if st.button('Login',icon=':material/passkey:',shortcut='control+enter',width='stretch'):
            if teacher_login(teacher_username,teacher_pass):
                st.toast("Welcome back!!",icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password!!")    

    with btnc2:
            if st.button('Register Instead',icon=':material/passkey:',type='primary',width='stretch'):
                st.session_state.teacher_login_type='register'


    footer_dashboard()

def register_teacher(teacher_username,teacher_name,teacher_pass,pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required!!"
    if check_teacher_exists(teacher_username):
        return False,"Username arealdy exists"
    if teacher_pass!=pass_confirm:
        return False,"Password doesn't match"
    try:
        create_teacher(teacher_username,teacher_pass,teacher_name)
        return True,"Teacher profile created successfully !! Login Now"
    except Exception as e:
        return False,f"Error creating teacher profile: {str(e)}"

    


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
        if st.button('Register now',icon=':material/passkey:',shortcut='control+enter',width='stretch'):
            success,message=register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type='login'
                st.rerun()
            else:
                st.error(message)    
    
    with btnc2:
        if st.button('Login Instead',icon=':material/passkey:',type='primary',width='stretch'):
            st.session_state.teacher_login_type='login'
        
    
    footer_dashboard()

 
    






