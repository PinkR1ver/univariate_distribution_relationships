import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
from ..utils import *
    
@st.cache_data
def erlang(k, mu, x_range):
    
    st.subheader('Erlang Distribution')
    
    erlang_distribution_plot(k, mu, x_range)
    
    content = '''The Erlang distribution is a continuous probability distribution that is a gamma distribution with integer values of the shape parameter. The probability density function of the Erlang distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{\mu^k x^{k-1} e^{-\mu x}}{(k-1)!}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = 1 - \sum_{i=0}^{k-1} \frac{e^{-\mu x} (\mu x)^i}{i!}'''
    st.latex(formula)
    
def erlang_distribution_plot(k, mu, x_range):
    
    fig1 = figure(title='Erlang Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Erlang Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')

    for i, (kk, mmu) in enumerate(zip(k, mu)):
    
            x = np.arange(0.001, x_range, 0.001)
            y = [mmu**kk * xx**(kk-1) * np.exp(-mmu*xx) / math.factorial(kk-1) for xx in x]
    
            fig1.line(x, y, line_width=2, legend_label=f'k={kk}, μ={mmu}', color=palette(i))
    
            step = x[1] - x[0]
            y = np.array(y)
            y = y * step
            
            fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'k={kk}, μ={mmu}', color=palette(i))
    
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)