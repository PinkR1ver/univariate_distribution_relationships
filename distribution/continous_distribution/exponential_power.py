import streamlit as st
import numpy as np
from bokeh.plotting import figure


@st.cache_data
def exponential_power(llambda , kappa, x_range):
    st.subheader('Exponential Power Distribution')
    
    x = np.arange(0.001, x_range, 0.001)
    y = [np.exp( 1 - np.exp(llambda * np.power(i, kappa))) * np.exp(llambda * np.power(i, kappa)) * llambda * kappa * np.power(i, kappa-1) for i in x]
    
    fig = figure(title='Exponential Power Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Exponential Power Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)

    formula = r'''\text{PDF}(x) = \left(e^{1 - e^{\lambda x^{\kappa}}} \right) e^{\lambda x^{\kappa}} \lambda \kappa x^{\kappa - 1}'''
    st.latex(formula)

    formula = r'''\text{CDF}(x) = 1 - e^{1 - e^{\lambda x^{\kappa}}}'''
    st.latex(formula)
    