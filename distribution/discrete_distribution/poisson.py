import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math
from ..utils import *

@st.cache_data
def poisson(t, llambda, k_range):
    
    st.subheader('Poisson Distribution')
    
    poisson_distribution_plot(t, llambda, k_range)

    
    formula = r'''\text{PDF}(k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}'''
    st.latex(formula)
    
    content = r'''Learn details about Poisson Distribution:'''
    st.markdown(content)
    
    content = r'''[Poisson Distribution](https://pinktalk.online/math/Statistics/basic_concepot/distribution/exponential_distribution_and_poisson_distribution)'''
    st.markdown(content)


@st.cache_data
def poisson_distribution_plot(t, llambda, k_range):
    
    fig1 = figure(title='Poisson Distribution PDF', x_axis_label='k', y_axis_label='Probability')
    fig2 = figure(title='Poisson Distribution CDF', x_axis_label='k', y_axis_label='Cumulative Probability')
    
    for i, (tt, lll) in enumerate(zip(t, llambda)):
    
        k = np.arange(0, k_range, 1)
        y = [np.exp(-lll * tt) * (lll * tt)**kk / math.factorial(kk) for kk in k]
    
        fig1.vbar(x=k, top=y, width=0.5, legend_label=f't={tt}, λ={lll}', line_width=2, color=palette(i), alpha=0.6)
        
        step = k[1] - k[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(k, np.cumsum(y), line_width=2, legend_label=f't={tt}, λ={lll}', color=palette(i))
    
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)