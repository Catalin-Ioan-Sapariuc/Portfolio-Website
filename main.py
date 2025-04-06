import streamlit as st

st.set_page_config(layout ="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Me_Iasi.png", width = 600)
    #width = 1000, height =2000)

with col2:
    st.header("Ioan Sapariuc")
    content="""
    I am a mathematician with a strong active interest in Data Analysis and Data Science.

    As a graduate student, I specialized in stiff high-speed reactive flows, modeled by the reactive Euler equations. 
    As part of this research, I developed fractional step finite volume methods, and conducted extensive analysis 
    of their accuracy and the stability. 

    In more recent years, I have transitioned to Python programming, and built end to end projects in areas 
    such as Recommender Systems and Natural Language Processing (NLP). I often use the power and simplicity of Python 
    to automate many tasks and to develop application. 

    I am deeply passionate about Data Science and Mathematics and I am eager to apply my expertise to impactful, 
    real world projects.

    I am also an avid lifelong learner, commited to staying current with the latest advancements in Data Science, 
    AI, and related fields, while enrolling in courses of interest in these areas. 

    Below you will find some of the projects I have built. Feel free to contact me! 
    """
    st.info(content)