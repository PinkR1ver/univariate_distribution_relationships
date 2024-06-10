import streamlit as st
import numpy as np
from bokeh.plotting import figure
import math



@st.cache_data
def gamma(alpha, beta, x_range):
    
    st.subheader('Gamma Distribution')
    
    x = np.arange(0.001, x_range, 0.001)
    y = [beta**alpha * i**(alpha-1) * np.exp(-beta*i) / math.gamma(alpha) for i in x]
    
    fig = figure(title='Gamma Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]  
    
    y = np.array(y)
    y = y * step
    
    
    fig = figure(title='Gamma Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = r'''Let ( $X_1$, $X_2$, ..., $X_n$ ) be the waiting times between consecutive events, and assume that these (n) waiting times are independent. The sum of these (n) waiting times, denoted as (Y) (i.e., ($Y = X_1 + X_2 + ... + X_n$)), follows a Gamma distribution, which can be expressed as:'''
    st.markdown(content)
    
    formula = r'''Y \sim \text{Gamma}(\theta, k)'''
    st.latex(formula)
    
    content = r'''or alternatively,'''
    st.markdown(content)
    
    formula = r'''Y \sim \text{Gamma}(\beta, \alpha)'''
    st.latex(formula)
    
    content = r'''Here, ($\alpha = n$), and ($\beta$) is the inverse of ($\theta$), where ($\theta$) represents the rate of event occurrence per unit time.'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{\beta^\alpha x^{\alpha-1} e^{-\beta x}}{\Gamma(\alpha)}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \int_0^x \frac{\beta^\alpha t^{\alpha-1} e^{-\beta t}}{\Gamma(\alpha)} dt = \frac{1}{\Gamma(\alpha)} \gamma(\alpha, \beta x)'''
    st.latex(formula)
    
    content = r'''Learn more details, see the link:'''
    st.markdown(content)

    link = '''[Gamma Distribution](https://pinktalk.online/math/Statistics/basic_concepot/distribution/gamma_distribution)'''
    st.markdown(link)
    