import streamlit as st
import pandas as pd
from io import StringIO
import numpy as np


# header
header = st.container()
with header:
    st.title('Story telling for parents') 

uploaded_file = st.file_uploader("Choose a file")

st.image(uploaded_file, caption='Sunrise by the mountains')


