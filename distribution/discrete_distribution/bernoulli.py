import streamlit as st
from bokeh.plotting import figure


@st.cache_data
def bernoulli(p):
    
    st.subheader('Benford Distribution')
    
    bernoulli_distribution_pdf(p)
    
    content = "The Bernoulli distribution is a discrete probability distribution that models a random experiment with two possible outcomes: success (1) and failure (0). The probability of success is denoted by $p$, while the probability of failure is $1 - p$. The probability mass function of the Bernoulli distribution is given by:"
    st.markdown(content)
    
    formula = r'''P(X = x) = \begin{cases} 1 - p & \text{if } x = 0 \\ p & \text{if } x = 1 \end{cases}'''
    st.latex(formula)


@st.cache_data
def bernoulli_distribution_pdf(p):
    
    x = [0, 1]
    y = [1 - p, p]

    fig = figure(title='Bernoulli Distribution', x_axis_label='Outcome', y_axis_label='Probability')
    fig.vbar(x=x, top=y, width=0.5)
    st.bokeh_chart(fig, use_container_width=True)