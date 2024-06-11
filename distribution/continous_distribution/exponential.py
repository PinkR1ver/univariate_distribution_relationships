import streamlit as st
import numpy as np
from bokeh.plotting import figure
from ..utils import *
    

@st.cache_data
def exponential(llambda, x_range):
    
    st.subheader('Exponential Distribution')
    
    exponential_distribution_plot(llambda, x_range)
    
    formula = r'''\text{PDF}(x) = \lambda e^{-\lambda x}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = 1 - e^{-\lambda x}'''
    st.latex(formula)
    
    
def exponential_distribution_plot(llambda, x_range):
    
    fig1 = figure(title='Exponential Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Exponential Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, l in enumerate(llambda):
    
        x = np.arange(0.001, x_range, 0.001)
        y = [l * np.exp(-l * i) for i in x]

        fig1.line(x, y, line_width=2, legend_label=f'λ={l}', color=palette(i))
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'λ={l}', color=palette(i))
        
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)