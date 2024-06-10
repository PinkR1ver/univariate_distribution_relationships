import streamlit as st
import numpy as np
from bokeh.plotting import figure


@st.cache_data
def gumbel(mu, beta, x_left_range, x_right_range):
    st.subheader('Gumbel Distribution')
    
    x = np.arange(x_left_range, x_right_range, 0.001)
    y = [(np.exp(-(np.exp(- (i - mu) / beta) + (i - mu) / beta)))/ beta for i in x]
    
    fig = figure(title='Gumbel Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Gumbel Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    formula = r'''\text{PDF}(x) = \left(e^{-\left(e^{-\frac{i-\mu}{\beta}} + \frac{i-\mu}{\beta}\right)}\right) / \beta'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = e^{-e^{-(x - \mu)/\beta}}'''
    st.latex(formula)
    

    
