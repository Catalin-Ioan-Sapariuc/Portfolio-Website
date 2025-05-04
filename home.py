import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout ="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Me_Iasi.png", width = 600)
    #width = 1000, height =2000)

with col2:
    st.header("Ioan Sapariuc")
    content="""
    I am a mathematician with a strong active interest in Data Analysis and Data Science.

    As a graduate student, I studied stiff high-speed reactive flows, modeled by the reactive Euler equations. 
    As part of this research, I developed fractional step finite volume methods, and conducted extensive analysis 
    of their accuracy and stability. 

    More recently, I have transitioned to Python programming, and built end to end projects in areas 
    such as Recommender Systems and Natural Language Processing (NLP). I often use the power and simplicity of Python 
    to automate many tasks and to develop application. 

    I am deeply passionate about Data Science and Mathematics and I am eager to apply my expertise to impactful, 
    real world projects.

    I am also an avid lifelong learner, commited to staying current with the latest advancements in Data Science, 
    AI, and related fields, while enrolling in courses of interest in these areas. 

    Below you will find some of the projects I have built. Feel free to contact me! 
    """
    st.info(content)

st.header("Past Projects:")

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=",")

with col3:
    for index, row in df.iterrows():
        if index < 6 and index%2 == 0:
            st.header(row['title'])
            st.write(row['description'])
            if index == 0:
                st.image("images/"+row['image'], width = 500)
                st.write("\n\n\n\n\n\n")
                st.write(f"[Source Code:]({row['urlsource']})")
                st.write(f"[Implemented Solution:]({row['urlsol']})")
                st.write("\n\n\n\n\n\n")
            else:
                st.image("images/"+row['image'])
            #st.image("images/"+ row['image'], width=400)
                st.write(f"[Source Code:]({row['urlsource']})")
                st.write(f"[Implemented Solution:]({row['urlsol']})")

with col4:
    for index, row in df.iterrows():
        if index < 6 and index%2 != 0:
            st.header(row['title'])
            st.write(row['description'])
            #st.image("images/"+ row['image'], width = 350)
            st.image("images/"+row['image'])
            st.write(f"[Source Code:]({row['urlsource']})")
            st.write(f"[Implemented Solution:]({row['urlsol']})")
