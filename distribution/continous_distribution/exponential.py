import streamlit as st
import numpy as np
from bokeh.plotting import figure
    

@st.cache_data
def exponential(llambda, x_range):
    
    st.subheader('Exponential Distribution')
    
    x = np.arange(0.001, x_range, 0.001)
    y = [llambda * np.exp(-llambda * i) for i in x]
    
    fig = figure(title='Exponential Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Exponential Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    formula = r'''\text{PDF}(x) = \lambda e^{-\lambda x}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = 1 - e^{-\lambda x}'''
    st.latex(formula)