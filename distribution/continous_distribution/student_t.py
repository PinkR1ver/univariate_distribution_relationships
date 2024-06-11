import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
from ..utils import *
    
@st.cache_data
def student_t(nu, x_left_range, x_right_range):
    
    st.subheader('Student\'s t Distribution')
    
    formula = r'''\text{PDF}(x) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \Gamma\left(\frac{\nu}{2}\right) \left(1 + \frac{x^2}{\nu}\right)^{\frac{\nu + 1}{2}}}'''
    st.latex(formula)
    
    
def student_t_distribution_plot(nu, x_left_range, x_right_range):
    
    fig1 = figure(title='Student\'s t Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    # fig2 = figure(title='Student\'s t Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, nn in enumerate(nu):
    
        x = np.arange(x_left_range, x_right_range, 0.001)
        y = [math.gamma((nn + 1) / 2) / (math.sqrt(nn * math.pi) * math.gamma(nn / 2) * (1 + xx**2 / nn)**((nn + 1) / 2)) for xx in x]
    
        fig1.line(x, y, line_width=2, legend_label=f'ν={nn}', color=palette(i))
        
    st.bokeh_chart(fig1, use_container_width=True)