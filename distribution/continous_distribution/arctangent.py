import streamlit as st
import numpy as np
from bokeh.plotting import figure
    
    
@st.cache_data
def artangent(llambda, theta, x_range):
    
    st.subheader('Artangent Distribution')
    
    x = np.arange(0, x_range, 0.001)
    y = [llambda / ((np.arctan(llambda * theta) + np.pi / 2) * (1 + llambda ** 2 * (i - theta) ** 2)) for i in x]
    
    fig = figure(title='Artangent Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = r'''Arctangent distribution is a continuous probability distribution that is symmetric about the mean and has a bell-shaped curve. The probability density function of the Arctangent distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{\lambda}{(\arctan(\lambda \theta) + \frac{\pi}{2})(1 + \lambda^2(x - \theta)^2)}'''
    st.latex(formula)