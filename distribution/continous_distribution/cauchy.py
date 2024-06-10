import streamlit as st
import numpy as np
from bokeh.plotting import figure


@st.cache_data
def cauchy(x0, gamma, x_left_range, x_right_range):
        
        st.subheader('Cauchy Distribution')
        
        x = np.arange(x_left_range, x_right_range, 0.001)
        y = [1 / (np.pi * gamma * (1 + ((i - x0) / gamma) ** 2)) for i in x]
        
        fig = figure(title='Cauchy Distribution', x_axis_label='x', y_axis_label='Probability Density')
        fig.line(x, y, line_width=2)
        st.bokeh_chart(fig, use_container_width=True)
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig = figure(title='Cauchy Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
        fig.line(x, np.cumsum(y), line_width=2)
        st.bokeh_chart(fig, use_container_width=True)
        
        formula = r'''\text{PDF}(x) = \frac{1}{\pi \gamma \left(1 + \left(\frac{x - x_0}{\gamma}\right)^2\right)}'''
        st.latex(formula)
        
        formula = r'''\text{CDF}(x) = \frac{1}{2} + \frac{1}{\pi} \arctan\left(\frac{x - x_0}{\gamma}\right)'''
        st.latex(formula)
        