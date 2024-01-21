import streamlit as st
import base64

st.title("Streamlit State Management xxxx")

"st.session_state objecct ", st.session_state
if "text" not in st.session_state:
    st.session_state["text"] = "hi"
if "file" not in st.session_state:
    st.session_state["file"] = None


def on_upper_clicked():
    if st.session_state.file is not None:
        #st.session_state.text = st.session_state.file.getvalue().upper()
        st.session_state.text = st.session_state.text.upper()
    else:      
        st.write("No file was uploaded")

st.text_area("Enter text", key="text")
st.header('Upload Image')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.image(uploaded_file)
    st.button("Upper Text", on_click=on_upper_clicked)
    #encoded_image = base64.b64encode(open(self.IMAGE_PATH, 'rb').read()).decode('ascii')
    encoded_image = base64.b64encode(uploaded_file.getvalue()).decode('ascii')
    st.write(encoded_image)
else:
    st.write('uploaded file will be displayed here')
        