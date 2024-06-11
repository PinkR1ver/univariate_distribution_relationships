
import streamlit as st
import numpy as np
from bokeh.plotting import figure
import scipy.integrate as spi
import math
from ..utils import *

@st.cache_data
def beta_binomial(a, b ,n):
    
    st.subheader('Beta-Binomial Distribution')
    
    beta_binomial_distribution_plot(a, b, n)
    
    content = '''The Beta-Binomial distribution is a compound probability distribution that combines the Beta distribution and the Binomial distribution. The Beta distribution is used to model the prior distribution of the probability of success in a Bernoulli trial, while the Binomial distribution models the likelihood of observing a certain number of successes in a fixed number of Bernoulli trials. The probability mass function of the Beta-Binomial distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''P(x) = \binom{n}{x} \frac{B(x + \alpha, n - x + \beta)}{B(\alpha, \beta)}'''
    st.latex(formula)
    
    formula = r'''B(\alpha, \beta) = \int_0^1 t^{\alpha - 1} (1 - t)^{\beta - 1} dt = \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)}'''
    st.latex(formula)
    
    link = '''[Serrano.Academy. The Beta Distribution in 12 Minutes! 2021. YouTube](https://www.youtube.com/watch?v=juF3r12nM5A)'''
    st.markdown(link)

    

@st.cache_data
def beta_binomial_distribution_plot(a, b, n):
    
    fig1 = figure(title='Beta-Binomial Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig2 = figure(title='Beta-Binomial Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')

    for i, (aa, bb) in enumerate(zip(a, b)):
        x = np.arange(0, n, 1)
        y = [math.comb(n, i) * beta(i + aa, n - i + bb) / beta(aa, bb) for i in x]
        
        fig1.vbar(x=x, top=y, width=0.5, legend_label=f'a={aa}, b={bb}', line_width=2, color=palette(i), alpha=0.6)
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig2.line(x, np.cumsum(y), line_width=2, legend_label=f'a={aa}, b={bb}', color=palette(i))
        
    st.bokeh_chart(fig1, use_container_width=True)
    st.bokeh_chart(fig2, use_container_width=True)
    
    
def beta(a, b):
    
    return spi.quad(lambda x: x**(a-1) * (1-x)**(b-1), 0, 1)[0]
