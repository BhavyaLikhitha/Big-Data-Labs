import streamlit as st
st.title("Hello, OrgAir!")
st.write("Welcome to the OrgAir platform.")
st.write("This is a simple Streamlit app running from app.py script.")


import pandas as pd
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
st.dataframe(df)

# st.text(input("Enter some text:", key="name"))


# st.session_state['name'] = st.text_input("Enter your name:")

add_selectbox = st.selectbox(
    "How would you like to be contacted?",  
    ("Email", "Home phone", "Mobile phone") 
)
st.write("You selected:", add_selectbox)

add_slider = st.slider(
    "Select a range of values", 0.0, 100.0, (25.0, 75.0)
)
st.write("Values:", add_slider)