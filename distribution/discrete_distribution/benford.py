import streamlit as st
import numpy as np
from bokeh.plotting import figure



@st.cache_data
def benford():
    
    st.subheader('Benford Distribution')

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [np.log10(1 + 1 / i) for i in x]

    p = figure(title='Benford Distribution', x_axis_label='Leading Digit', y_axis_label='Frequency')
    p.line(x, y, line_width=2)
    st.bokeh_chart(p, use_container_width=True)

    content = "Benford Distribution, also known as Benford's Law, is a law concerning the frequency of appearance of the leading digits in a set of natural numbers. It states that in many naturally occurring collections of numerical data, the probability of smaller digits appearing as the leading digit is higher. Specifically, Benford's Law predicts that the number 1 appears as the leading digit with a probability of about 30%, while the number 9 appears as the leading digit with a probability of only about 4.6%. This distribution pattern can be expressed with the following formula:"
    st.markdown(content)

    formula = r'''P(d) = \log_{10}\left(1 + \frac{1}{d}\right)'''
    st.latex(formula)

    content = '''where $d$ is an integer between 1 and 9 (the leading digit), and $P(d)$ is the probability of $d$ appearing as the leading digit.'''
    st.markdown(content)

    content = '''Benford's Law has applications in various fields, including but not limited to accounting and auditing, physics, astronomy, and social sciences. It can be used to :blue-background[detect] :red[anomalies] or :red[fraudulent] behaviors in data sets, as artificially constructed data often does not conform to the distribution predicted by Benford's Law. Additionally, Benford's Law is used in scientific data analysis to help researchers verify the natural growth or distribution characteristics of data.'''
    st.markdown(content)