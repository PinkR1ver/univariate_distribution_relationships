import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math


@st.cache_data
def poisson(t, llambda, k_range):
    
    st.subheader('Poisson Distribution')
    
    k = np.arange(0, k_range, 1)
    y = [np.exp(-llambda * t) * (llambda * t)**i / math.factorial(i) for i in k]
    
    fig = figure(title='Poisson Distribution', x_axis_label='k', y_axis_label='Probability')
    fig.vbar(x=k, top=y, width=0.5)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = k[1] - k[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Poisson Distribution CDF', x_axis_label='k', y_axis_label='Cumulative Probability')
    fig.line(k, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    formula = r'''\text{PDF}(k) = \frac{e^{-\lambda t}(\lambda t)^k}{k!}'''
    st.latex(formula)
    
    content = r'''Learn details about Poisson Distribution:'''
    st.markdown(content)
    
    content = r'''[Poisson Distribution](https://pinktalk.online/math/Statistics/basic_concepot/distribution/exponential_distribution_and_poisson_distribution)'''
    st.markdown(content)