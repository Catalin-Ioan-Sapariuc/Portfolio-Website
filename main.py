import streamlit as st

st.set_page_config(layout ="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Me_Iasi.png", width = 700)
    #width = 1000, height =2000)

with col2:
    st.header("Ioan Sapariuc")
    content="""
    I am a mathematician with a strong interest and practice in Data Analysis and Data Science. \
    I hold a BS degree in Mathematics and Mechanics from A.I. Cuza University,  which is in Iași, Romania, 
    and a PhD degree in Mathematics from Rensselaer Polytechnic Institute, located in Troy, New York. 

    As a Python Programmer, I have successfully built a few end to end projects in areas such as Recommender 
    Systems and Natural Language Processing (NLP).
    I am also using Python to automate many tasks and to build various apps. 
    I am eager to apply my expertise and passion for Data Science, Data Analysis, and Mathematics 
    to contribute to impactful projects in these fields..
    """
    st.info(content)