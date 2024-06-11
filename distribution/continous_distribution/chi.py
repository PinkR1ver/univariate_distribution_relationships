import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
from ..utils import *

@st.cache_data
def chi(n, x_range):
    
    st.subheader('Chi Distribution')
    
    chi_distribution_plot(n, x_range)
    
    formula = r'''\text{PDF}(x) = \frac{x^{n-1} e^{-\frac{x^2}{2}}}{2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right)}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \int_0^x \frac{t^{n-1} e^{-\frac{t^2}{2}}}{2^{\frac{n}{2}-1} \Gamma\left(\frac{n}{2}\right)} dt = \frac{1}{\Gamma\left(\frac{n}{2}\right)} \gamma\left(\frac{n}{2}, \frac{x^2}{2}\right)'''
    st.latex(formula)
    
def chi_distribution_plot(n, x_range):
    
    fig1 = figure(title='Chi Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Chi Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, nn in enumerate(n):
    
        x = np.arange(0, x_range, 0.001)
        y = [xx**(nn-1) * np.exp(-xx**2 / 2) / (2**(nn/2-1) * math.gamma(float(nn/2))) for xx in x]
    
        fig1.line(x, y, line_width=2, legend_label=f'n={nn}', color=palette(i))
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'n={nn}', color=palette(i))
        
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)