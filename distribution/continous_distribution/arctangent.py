import streamlit as st
import numpy as np
from bokeh.plotting import figure
from ..utils import *
    
@st.cache_data
def artangent(llambda, theta, x_range):
    
    st.subheader('Artangent Distribution')
    
    arctangent_distribution_plot(llambda, theta, x_range)
    
    content = r'''Arctangent distribution is a continuous probability distribution that is symmetric about the mean and has a bell-shaped curve. The probability density function of the Arctangent distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{\lambda}{(\arctan(\lambda \theta) + \frac{\pi}{2})(1 + \lambda^2(x - \theta)^2)}'''
    st.latex(formula)
    

def arctangent_distribution_plot(llambda, theta, x_range):
    
    fig1 = figure(title='Artangent Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Artangent Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    
    for i, (ll, th) in enumerate(zip(llambda, theta)):
        x = np.arange(0, x_range, 0.001)
        y = [ll / ((np.arctan(ll * th) + np.pi / 2) * (1 + ll ** 2 * (xx - th) ** 2)) for xx in x]
        
        fig1.line(x, y, line_width=2, legend_label=f'λ={ll}, Θ={th}', color=palette(i))
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'λ={ll}, Θ={th}', color=palette(i))

    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)