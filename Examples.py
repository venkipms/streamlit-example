# Example 1
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# Example 2
import streamlit as st
import pandas as pd

st.write("First Attempt in using Data to create Table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Example 3
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# Example 4
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

# Example 5
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Example 6
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Example 7
import streamlit as st

X = st.slider('x')  # It's a widget
st.write('Slider Value =', X, 'Squared Value = ', X * X)

# Example 7
import streamlit as st

st.text_input("Name", key="name")
st.text_input("Age", key='age')
st.text_input("University", key='univ')

# You can access the value at any point with:
st.session_state.name
st.session_state.age
st.session_state.univ

# Example 8
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20, 3),
                                    columns=['a', 'b', 'c'])
    chart_data

    
