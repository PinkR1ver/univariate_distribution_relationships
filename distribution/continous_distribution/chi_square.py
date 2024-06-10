import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math

@st.cache_data
def chi_square(n, x_range):
    
    st.subheader('Chi-Square Distribution')
    
    x = np.arange(0.001, x_range, 0.001)
    y = [x**(n/2-1) * np.exp(-x/2) / (2**(n/2) * math.gamma(n/2)) for x in x]
    
    fig = figure(title='Chi-Square Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Chi-Square Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = r'''Let ( $X_1$, $X_2$, ..., $X_n$ ) be independent and identically distributed standard normal random variables. The sum of the squares of these random variables, denoted as (Y) (i.e., ($Y = X_1^2 + X_2^2 + ... + X_n^2$)), follows a Chi-Square distribution with $n$ degrees of freedom, which can be expressed as:'''
    st.markdown(content)
    
    formula = r'''Y \sim \chi^2(n)'''
    st.latex(formula)
    
    content = r'''The probability density function (PDF) of the Chi-Square distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{x^{\frac{n}{2}-1} e^{-\frac{x}{2}}}{2^{\frac{n}{2}} \Gamma\left(\frac{n}{2}\right)}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \int_0^x \frac{t^{\frac{n}{2}-1} e^{-\frac{t}{2}}}{2^{\frac{n}{2}} \Gamma\left(\frac{n}{2}\right)} dt = \frac{1}{\Gamma\left(\frac{n}{2}\right)} \gamma\left(\frac{n}{2}, \frac{x}{2}\right)'''
    st.latex(formula)