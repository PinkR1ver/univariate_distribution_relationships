import streamlit as st
import numpy as np
from bokeh.plotting import figure
    

@st.cache_data
def arcsin():
    
    st.subheader('Arcsin Distribution')
    
    arcsin_distribution_plot()
    
    content = '''The Arcsin distribution is a continuous probability distribution that is symmetric about the mean and has a bell-shaped curve. The probability density function of the Arcsin distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{1}{\pi \sqrt{x(1-x)}}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \frac{2}{\pi} \arcsin(\sqrt{x})'''
    st.latex(formula)
    
    
def arcsin_distribution_plot():
    
    x = np.arange(0.001, 1, 0.001)
    y = [1 / (np.pi * np.sqrt(i * (1 - i))) for i in x]
    
    fig = figure(title='Arcsin Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Arcsin Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)