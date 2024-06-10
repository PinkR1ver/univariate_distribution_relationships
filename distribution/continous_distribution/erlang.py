import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
    
@st.cache_data
def erlang(k, mu, x_range):
    
    st.subheader('Erlang Distribution')
    
    x = np.arange(0.001, x_range, 0.001)
    y = [mu**k * i**(k-1) * np.exp(-mu*i) / math.factorial(k-1) for i in x]
    
    fig = figure(title='Erlang Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Erlang Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)