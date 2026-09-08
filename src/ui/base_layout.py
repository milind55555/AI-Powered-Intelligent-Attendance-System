import streamlit as st


def style_base_home():
    st.markdown(
        """
        <style>

        .stApp {
        background: linear-gradient(
        135deg,
        #D8B4FE,
        #C4B5FD,
        #A78BFA
        );
        }

        .stApp div[data-testid="stColumn"] {
            background-color:#E0E3FF !important;
            padding:2.5rem !important;
            border-radius: 5rem !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_dashboard():
    st.markdown(
        """
        <style>

        .stApp {
            background: linear-gradient(
            135deg,
            #E6FFFA 0%,
            #E0F2FE 50%,
            #ECFDF5 100%
        );
        }

        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


        /* Hide top bar of streamlit */
        #MainMenu,footer,header{
        visibility:hidden;
        }
        .block-container{
            padding-top:1.5rem !important;
        }

        h1{
        font-family: "Climate Crisis", sans-serif !important;
        font-size:3.5rem !important;
        line-height:1.1 impportant;
        margin-bottom:0rem !important;
        color:#28282B !important;
        }

        h2{
        font-family: "Climate Crisis", sans-serif !important;
        font-size:2rem !important;
        line-height:0.9 impportant;
        margin-bottom:0rem !important;
        color:#28282B !important;

        }

        h3,h4,p {
        font-family:'Outfit',sans-serif;
        }

        button{
            border-radius:1.5rem !important;
            background: #4F46E5 !important;
            color: #FFFFFF !important;
            padding:10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"]{
            border-radius:1.5rem !important;
            background: #0F766E !important;
            color: #FFFFFF !important;
            padding:10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="Tertiary"]{
                    border-radius:1.5rem !important;
                    background: #EA580C !important;
                    color: #FFFFFF !important;
                    padding:10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
        transform:scale(1.05)
        }
        

        </style>
        """,
        unsafe_allow_html=True
    )