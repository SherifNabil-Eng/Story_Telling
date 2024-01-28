import streamlit as st

head = st.container()
with head:
    st.title('Story telling Test')
    st.write('This is a test for uploading files to a streamlit app')

title = st.container()
with title:
    st.header('Upload Image')
    uploaded_file = st.file_uploader("Choose a file")