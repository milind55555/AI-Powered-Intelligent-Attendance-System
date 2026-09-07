import streamlit as st

def  style_base_layout():
    st.markdown(
        """
        <style>
        .stApp{
            background: #5865f2 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def  style_base_background():
    st.markdown(
        """
        <style>
        .css-1d391kg {
            background-color: #f5f5f5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )