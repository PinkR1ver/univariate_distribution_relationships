import streamlit as st
import numpy as np
from bokeh.plotting import figure
from ..utils import *


@st.cache_data
def cauchy(x0, gamma, x_left_range, x_right_range):
        
        st.subheader('Cauchy Distribution')
        
        cauchy_distribution_plot(x0, gamma, x_left_range, x_right_range)
        
        formula = r'''\text{PDF}(x) = \frac{1}{\pi \gamma \left(1 + \left(\frac{x - x_0}{\gamma}\right)^2\right)}'''
        st.latex(formula)
        
        formula = r'''\text{CDF}(x) = \frac{1}{2} + \frac{1}{\pi} \arctan\left(\frac{x - x_0}{\gamma}\right)'''
        st.latex(formula)
        
def cauchy_distribution_plot(x0, gamma, x_left_range, x_right_range):
        
        fig1 = figure(title='Cauchy Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
        fig2 = figure(title='Cauchy Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')

        for i, (xx0, gg) in enumerate(zip(x0, gamma)):
        
                x = np.arange(x_left_range, x_right_range, 0.001)
                y = [1 / (np.pi * gg * (1 + ((xx - xx0) / gg) ** 2)) for xx in x]
        
                fig1.line(x, y, line_width=2, legend_label=f'x0={xx0}, γ={gg}', color=palette(i))

                y = [0.5 + (1 / np.pi) * np.arctan((xx - xx0) / gg) for xx in x]
                
                fig2.line(x, y, line_width=2, legend_label=f'x0={xx0}, γ={gg}', color=palette(i))
        
        st.bokeh_chart(fig1, use_container_width=True)
        st.bokeh_chart(fig2, use_container_width=True)
        