import streamlit
import pandas

my_fruit_list=read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My parents new healthy diner')
streamlit.header('blabla menu')

streamlit.text('blablabla')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
