import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20, 3),
                                    columns=['a', 'b', 'c'])
    chart_data


