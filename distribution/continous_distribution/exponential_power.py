import streamlit as st
import numpy as np
from bokeh.plotting import figure
from ..utils import *


@st.cache_data
def exponential_power(llambda , kappa, x_range):
    st.subheader('Exponential Power Distribution')
    
    exponential_power_distribution_plot(llambda , kappa, x_range)

    formula = r'''\text{PDF}(x) = \left(e^{1 - e^{\lambda x^{\kappa}}} \right) e^{\lambda x^{\kappa}} \lambda \kappa x^{\kappa - 1}'''
    st.latex(formula)

    formula = r'''\text{CDF}(x) = 1 - e^{1 - e^{\lambda x^{\kappa}}}'''
    st.latex(formula)


def exponential_power_distribution_plot(llambda , kappa, x_range):
    
    fig1 = figure(title='Exponential Power Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Exponential Power Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, (ll, kk) in enumerate(zip(llambda , kappa)):
        
        x = np.arange(0.001, x_range, 0.001)
        y = [np.exp( 1 - np.exp(ll * np.power(xx, kk))) * np.exp(ll * np.power(xx, kk)) * ll * kk * np.power(xx, kk-1) for xx in x]
    
        fig1.line(x, y, line_width=2, legend_label=f'λ={ll}, κ={kk}', color=palette(i))
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'λ={ll}, κ={kk}', color=palette(i))
    
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)    

    