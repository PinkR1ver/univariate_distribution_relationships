import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
        

@st.cache_data
def chi(n, x_range):
    
    st.subheader('Chi Distribution')
    
    x = np.arange(0, x_range, 0.001)
    y = [x**(n-1) * np.exp(-x**2 / 2) / (2**(n/2-1) * math.gamma(float(n/2))) for x in x]
    
    fig = figure(title='Chi Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Chi Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    formula = r'''\text{PDF}(x) = \frac{x^{n-1} e^{-\frac{x^2}{2}}}{2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right)}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \int_0^x \frac{t^{n-1} e^{-\frac{t^2}{2}}}{2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right)} dt = \frac{1}{\Gamma\left(\frac{n}{2}\right)} \gamma\left(\frac{n}{2}, \frac{x^2}{2}\right)'''
    st.latex(formula)