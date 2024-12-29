import streamlit as st
import pandas as pd
import numpy as np

st.title('hello')

st.divider()
name = st.text_input('name')
animal = st.selectbox('animal', ['dog', 'cat', 'squirrel', 'dolphin'])
st.divider()
color = st.color_picker('Pick a color', '#5b6ee6')
st.divider()
st.write('{} likes a {} {}'.format(name, color, animal))
