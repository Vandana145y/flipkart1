import streamlit as st
from datetime import datetime, date , time

language = st.selectbox(
    "What is your fav programming language",
    ["C", "C++", "Python", "Java", "C#"]
)

st.write(f"My fav programming language is {language}")

st.header("Multi select boxes")
language = st.multiselect(
    "What is your fav programming language",
    ["C", "C++", "Python", "Java", "C#"]
)

st.write(f"My fav programming language is {language}")

st.header("select Slider")

review=st.select_slider("Movie Rating",
                        ["Worst","Bad","Average","Good","Best"])
st.write(f"Movie Ratings : {review}")

st.header("Slider")
height=st.slider("my height is cms",min_value=0,max_value=500)
st.write(f"my height in cms is :{height}")

st.header("Text input")
name=st.text_input("What is your name")
st.write(f"My name is :{name}")

st.header("Text Area")
feedback=st.text_area("Write your feedback here : ")
st.write(f"My feedback is : {feedback}")

st.header("Number input")
age=st.number_input("What is your age",min_value=0,max_value=200)

st.write(f"My age is {age}")

st.header("Date ")
dob=st.date_input("what is your date of birth",min_value=datetime(1990,1,1),max_value=datetime(2026,1,31)
)
st.write("my date of birth is : {dob}")

