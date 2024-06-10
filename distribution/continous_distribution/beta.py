import streamlit as st
import numpy as np
from bokeh.plotting import figure
import scipy.integrate as spi
    
@st.cache_data
def beta_distribution(a, b):
    
    st.subheader('Beta Distribution')
    
    x = np.arange(0.001, 1, 0.001)
    y = [i**(a-1) * (1-i)**(b-1) for i in x]
    y = np.array(y)
    y = y / beta(a, b)
    
    fig = figure(title='Beta Distribution PDF', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Beta Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = r'''Beta distribution is a probability probability distribution that stretches the distribution into different shapes by two parameters, $\alpha$ and $\beta$. $\alpha$ and $\beta$ can be obtained from experiments, so we can predict the probability of an event occurring from a large number of experiments P. The vivid visualization can be seen in the link below'''
    st.markdown(content)
    
    content = r'''Meanwhile, the Beta function can be related to classical distributions such as :blue-background[Arcsin distribution], :blue-background[Standard Uniform distribution], :blue-background[Gamma distribution], etc. by adjusting the parameters of alpha and beta'''
    st.markdown(content)
    
    content = r'''The probability density function (PDF) of the Beta distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(\theta |\alpha,\beta) = \frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{Beta(\alpha, \beta)}'''
    st.latex(formula)
    
    formula = r'''\text{Beta}(\alpha, \beta) = \int_0^1 \theta^{\alpha-1}(1-\theta)^{\beta-1} d\theta'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(\theta |\alpha,\beta) = \int_0^\theta \frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{Beta(\alpha, \beta)} d\theta'''
    st.latex(formula)
    
    content = '''Here's the link to the vivid explanation of the Beta Distribution:'''
    st.markdown(content)
    
    link = '''[Serrano.Academy. The Beta Distribution in 12 Minutes! 2021. YouTube](https://www.youtube.com/watch?v=juF3r12nM5A)'''
    st.markdown(link)
    
def beta(a, b):
    
    return spi.quad(lambda x: x**(a-1) * (1-x)**(b-1), 0, 1)[0]
