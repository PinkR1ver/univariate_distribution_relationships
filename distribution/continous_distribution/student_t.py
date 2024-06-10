import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
    
@st.cache_data
def student_t(nu, x_left_range, x_right_range):
    
    st.subheader('Student\'s t Distribution')
    
    x = np.arange(x_left_range, x_right_range, 0.001)
    y = [math.gamma((nu + 1) / 2) / (math.sqrt(nu * math.pi) * math.gamma(nu / 2) * (1 + i**2 / nu)**((nu + 1) / 2)) for i in x]
    
    fig = figure(title='Student\'s t Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Student\'s t Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    formula = r'''\text{PDF}(x) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \Gamma\left(\frac{\nu}{2}\right) \left(1 + \frac{x^2}{\nu}\right)^{\frac{\nu + 1}{2}}}'''
    st.latex(formula)