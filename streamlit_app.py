import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [30, 30] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
