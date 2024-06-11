import streamlit as st
import numpy as np
from bokeh.plotting import figure
from ..utils import *


@st.cache_data
def gumbel(mu, beta, x_left_range, x_right_range):
    
    st.subheader('Gumbel Distribution')
    
    gumbel_distribution_plot(mu, beta, x_left_range, x_right_range)
    
    formula = r'''\text{PDF}(x) = \left(e^{-\left(e^{-\frac{i-\mu}{\beta}} + \frac{i-\mu}{\beta}\right)}\right) / \beta'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = e^{-e^{-(x - \mu)/\beta}}'''
    st.latex(formula)
    
def gumbel_distribution_plot(mu, beta, x_left_range, x_right_range):
    
    fig1 = figure(title='Gumbel Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Gumbel Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, (mm, bb) in enumerate(zip(mu, beta)):
        
        x = np.arange(x_left_range, x_right_range, 0.001)
        y = [(np.exp(-(np.exp(- (xx - mm) / bb) + (xx - mm) / bb)))/ bb for xx in x]
        
        fig1.line(x, y, line_width=2, legend_label=f'μ={mm}, β={bb}', color=palette(i))
        
        y = [np.power(np.e, -np.power(np.e, -(xx - mm)/bb)) for xx in x]
        
        fig2.line(x, y, line_width=2, legend_label=f'μ={mm}, β={bb}', color=palette(i))
        
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)
        
    

    
