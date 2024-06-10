
import streamlit as st
import numpy as np
from bokeh.plotting import figure
import scipy.integrate as spi
import math

    

@st.cache_data
def beta_binomial(a, b, n):
    
    st.subheader('Beta-Binomial Distribution')

    x = np.arange(0, n, 1)
    y = [math.comb(n, i) * beta(i + a, n - i + b) / beta(a, b) for i in x]
        
    fig = figure(title='Beta-Binomial Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.vbar(x=x, top=y, width=0.5)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]   
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Beta-Binomial Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = '''The Beta-Binomial distribution is a compound probability distribution that combines the Beta distribution and the Binomial distribution. The Beta distribution is used to model the prior distribution of the probability of success in a Bernoulli trial, while the Binomial distribution models the likelihood of observing a certain number of successes in a fixed number of Bernoulli trials. The probability mass function of the Beta-Binomial distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''P(x) = \binom{n}{x} \frac{B(x + \alpha, n - x + \beta)}{B(\alpha, \beta)}'''
    st.latex(formula)
    
    formula = r'''B(\alpha, \beta) = \int_0^1 t^{\alpha - 1} (1 - t)^{\beta - 1} dt = \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)}'''
    st.latex(formula)
    
    link = '''[Serrano.Academy. The Beta Distribution in 12 Minutes! 2021. YouTube](https://www.youtube.com/watch?v=juF3r12nM5A)'''
    st.markdown(link)
    
def beta(a, b):
    
    return spi.quad(lambda x: x**(a-1) * (1-x)**(b-1), 0, 1)[0]
