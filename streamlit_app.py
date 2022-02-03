import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [60, 70],
    columns=['lat', 'lon'])

st.map(map_data)
