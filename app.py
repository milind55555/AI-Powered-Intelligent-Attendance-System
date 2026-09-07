import streamlit as st

def main():
    st.header("This is header")
    name = st.text_input("Enter your name?",key="input1")

    col1,col2=st.columns(2,gap="small")
    with col1:
        if st.button("Hiiii",type="primary",key="btn1",width="stretch"):
            print("Hiiii",name)
    with col2:
        if st.button("Byeee",type="primary",key="btn2",width="stretch"):
            print("Byeee",name)        
    st.markdown("""
    <style>
        button{
                background: orange!important;}        
    </style>

    """,unsafe_allow_html=True)
main()   