import streamlit
streamlit.title('My Parents New Healty Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Utwórz listę etykiet na podstawie kolumny 'Fruit'
fruit_labels = list(my_fruit_list['Fruit'])
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", fruit_labels)

# Display the table on the page
streamlit.dataframe(my_fruit_list)
