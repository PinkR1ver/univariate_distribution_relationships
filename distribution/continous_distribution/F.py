import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
from ..utils import *

 
@st.cache_data
def F(d1, d2, x_range):
    st.subheader('F Distribution')
    
    F_distribution_plot(d1, d2, x_range)
    
    formula = r'''\text{PDF}(x) = \frac{\Gamma\left(\frac{d1 + d2}{2}\right) \left(\frac{d1}{d2}\right)^{\frac{d1}{2}} x^{\frac{d1}{2}-1}}{\Gamma\left(\frac{d1}{2}\right) \Gamma\left(\frac{d2}{2}\right) \left(1 + \frac{d1}{d2} x \right)^{\frac{d1 + d2}{2}}}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \int_0^x \text{PDF}(t) dt'''
    st.latex(formula)
    
    content = r'''The relationship of Gamma function and Beta function:'''
    st.markdown(content)
    
    formula = r'''\Beta(x, y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}'''
    st.latex(formula)
    
    content = r'''Thus, the PDF of the F distribution can be also expressed as:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{\left(\frac{d1}{d2}\right)^{\frac{d1}{2}}x^{\frac{d1}{2}-1} }{ \Beta \left(\frac{d1}{2}, \frac{d2}{2}\right) \left(1 + \frac{d1}{d2} x \right)^{\frac{d1 + d2}{2}}}'''
    st.latex(formula)
    
def F_distribution_plot(d1, d2, x_range):
    
    fig1 = figure(title='F Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='F Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, (dd1, dd2) in enumerate(zip(d1, d2)):
    
        x = np.arange(0.001, x_range, 0.001)
        y = [math.gamma((dd1 + dd2) / 2) * np.power(dd1 / dd2, dd1 / 2) * np.power(xx, dd1 / 2 - 1) / (math.gamma(dd1 / 2) * math.gamma(dd2 / 2) * np.power(1 + dd1 * xx / dd2, (dd1 + dd2) / 2)) for xx in x]
    
        fig1.line(x, y, line_width=2, legend_label=f'd1={dd1}, d2={dd2}', color=palette(i))
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'd1={dd1}, d2={dd2}', color=palette(i))
        
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)