import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import scipy.integrate as spi
import math



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

@st.cache_data
def bernoulli(p):
    
    st.subheader('Benford Distribution')
    
    x = [0, 1]
    y = [1 - p, p]

    fig = figure(title='Bernoulli Distribution', x_axis_label='Outcome', y_axis_label='Probability')
    fig.vbar(x=x, top=y, width=0.5)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = "The Bernoulli distribution is a discrete probability distribution that models a random experiment with two possible outcomes: success (1) and failure (0). The probability of success is denoted by $p$, while the probability of failure is $1 - p$. The probability mass function of the Bernoulli distribution is given by:"
    st.markdown(content)
    
    formula = r'''P(X = x) = \begin{cases} 1 - p & \text{if } x = 0 \\ p & \text{if } x = 1 \end{cases}'''
    st.latex(formula)
    

@st.cache_data
def arcsin():
    
    st.subheader('Arcsin Distribution')
    
    x = np.arange(0.001, 1, 0.001)
    y = [1 / (np.pi * np.sqrt(i * (1 - i))) for i in x]
    
    fig = figure(title='Arcsin Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Arcsin Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = '''The Arcsin distribution is a continuous probability distribution that is symmetric about the mean and has a bell-shaped curve. The probability density function of the Arcsin distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{1}{\pi \sqrt{x(1-x)}}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \frac{2}{\pi} \arcsin(\sqrt{x})'''
    st.latex(formula)
    
    
@st.cache_data
def artangent(llambda, theta):
    
    st.subheader('Artangent Distribution')
    
    x = np.arange(0.01, 10, 0.01)
    y = [llambda / ((np.arctan(llambda * theta) + np.pi / 2) * (1 + llambda ** 2 * (i - theta) ** 2)) for i in x]
    
    fig = figure(title='Artangent Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    content = r'''Arctangent distribution is a continuous probability distribution that is symmetric about the mean and has a bell-shaped curve. The probability density function of the Arctangent distribution is given by the following formula:'''
    st.markdown(content)
    
    formula = r'''\text{PDF}(x) = \frac{\lambda}{(\arctan(\lambda \theta) + \frac{\pi}{2})(1 + \lambda^2(x - \theta)^2)}'''
    st.latex(formula)

def beta_binomial(a, b, n):
    
    st.subheader('Beta-Binomial Distribution')

    x = np.arange(0, n, 1)
    y = [math.comb(20, i) * beta(i + a, 20 - i + b) / beta(a, b) for i in x]
        
    fig = figure(title='Beta-Binomial Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
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
    
@st.cache_data
def poisson(t, llambda):
    
    st.subheader('Poisson Distribution')
    
    k = np.arange(0, 20, 1)
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
    
@st.cache_data
def cauchy(x0, gamma):
        
        st.subheader('Cauchy Distribution')
        
        x = np.arange(-10, 10, 0.001)
        y = [1 / (np.pi * gamma * (1 + ((i - x0) / gamma) ** 2)) for i in x]
        
        fig = figure(title='Cauchy Distribution', x_axis_label='x', y_axis_label='Probability Density')
        fig.line(x, y, line_width=2)
        st.bokeh_chart(fig, use_container_width=True)
        
        step = x[1] - x[0]
        y = np.array(y)
        y = y * step
        
        fig = figure(title='Cauchy Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
        fig.line(x, np.cumsum(y), line_width=2)
        st.bokeh_chart(fig, use_container_width=True)
        
        formula = r'''\text{PDF}(x) = \frac{1}{\pi \gamma \left(1 + \left(\frac{x - x_0}{\gamma}\right)^2\right)}'''
        st.latex(formula)
        
        formula = r'''\text{CDF}(x) = \frac{1}{2} + \frac{1}{\pi} \arctan\left(\frac{x - x_0}{\gamma}\right)'''
        st.latex(formula)
        

@st.cache_data
def chi(n):
    
    st.subheader('Chi Distribution')
    
    x = np.arange(0.001, 10, 0.001)
    y = [x**(n-1) * np.exp(-x**2 / 2) / (2**(n/2-1) * math.factorial(n-1)) for x in x]
    
    fig = figure(title='Chi Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Chi Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    formula = r'''\text{PDF}(x) = \frac{x^{n-1} e^{-\frac{x^2}{2}}}{2^{\frac{n}{2}-1} (n-1)!}'''
    st.latex(formula)
    
    formula = r'''\text{CDF}(x) = \int_0^x \frac{t^{n-1} e^{-\frac{t^2}{2}}}{2^{\frac{n}{2}-1} (n-1)!} dt = \frac{1}{\Gamma\left(\frac{n}{2}\right)} \gamma\left(\frac{n}{2}, \frac{x^2}{2}\right)'''
    st.latex(formula)
    

@st.cache_data
def chi_square(n):
    
    st.subheader('Chi-Square Distribution')
    
    x = np.arange(0.001, 20, 0.001)
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
    
@st.cache_data
def gamma(alpha, beta):
    
    st.subheader('Gamma Distribution')
    
    x = np.arange(0.001, 20, 0.001)
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
    
    
@st.cache_data
def erlang(k, mu):
    
    st.subheader('Erlang Distribution')
    
    x = np.arange(0.001, 20, 0.001)
    y = [mu**k * i**(k-1) * np.exp(-mu*i) / math.factorial(k-1) for i in x]
    
    fig = figure(title='Erlang Distribution', x_axis_label='x', y_axis_label='Probability Density')
    fig.line(x, y, line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    step = x[1] - x[0]
    y = np.array(y)
    y = y * step
    
    fig = figure(title='Erlang Distribution CDF', x_axis_label='x', y_axis_label='Cumulative Probability')
    fig.line(x, np.cumsum(y), line_width=2)
    st.bokeh_chart(fig, use_container_width=True)
    
    
    
    
    
    
    
if __name__ == '__main__':

    with st.sidebar:
        st.title('All Univariate Distribution')
        
        add_selectbox1 = st.selectbox(
            'Select a Distribution',
            ('Discrete Distributions', 'Continuous Distributions')
        )
        
        if add_selectbox1 == 'Discrete Distributions':
            add_selectbox2 = st.selectbox(
                'Select a Distribution',
                ('Benford Distribution', 'Bernoulli Distribution', 'Beta-Binomial Distribution',
                 'Poisson Distribution')
            )
            
            if add_selectbox2 == 'Bernoulli Distribution':
                p = st.slider('Probability of Success (p)', 0.0, 1.0, 0.5)
                
            elif add_selectbox2 == 'Beta-Binomial Distribution':
                a = st.slider('Shape Parameter (a)', 0.1, 10.0, 1.0)
                b = st.slider('Shape Parameter (b)', 0.1, 10.0, 1.0)
                n = st.slider('Number of Trials (n)', 1, 20, 1)
                
            elif add_selectbox2 == 'Poisson Distribution':
                llambda = st.slider('Rate Parameter (λ)', 0.1, 10.0, 1.0)
                t = st.slider('Time Interval (t)', 0.1, 10.0, 1.0)
            
        elif add_selectbox1 == 'Continuous Distributions':
            add_selectbox2 = st.selectbox(
                'Select a Distribution',
                ('Arcsin Distribution', 'Arctangent Distribution', 'Beta Distribution', 
                 'Cauchy Distribution', 'Chi Distribution', 'Chi-square Distribution', 
                 'Erlang Distribution', 'Gamma Distribution')
            )
            
            if add_selectbox2 == 'Beta Distribution':
                a = st.slider('Shape Parameter (a)', 0.1, 100.0, 1.0)
                b = st.slider('Shape Parameter (b)', 0.1, 100.0, 1.0)
                
            elif add_selectbox2 == 'Arctangent Distribution':
                llambda = st.slider('Shape Parameter (λ)', 0.1, 10.0, 1.0)
                theta = st.slider('Shape Parameter (θ)', 0.1, 10.0, 1.0)
                
            elif add_selectbox2 == 'Cauchy Distribution':
                x0 = st.slider('Location Parameter (x0)', -10.0, 10.0, 0.0)
                gamma = st.slider('Scale Parameter (γ)', 0.1, 10.0, 1.0)
                
            elif add_selectbox2 == 'Chi Distribution':
                n = st.slider('Degrees of Freedom (n)', 1, 10, 1)
            
            elif add_selectbox2 == 'Chi-square Distribution':
                n = st.slider('Degrees of Freedom (n)', 1, 10, 1)
                
            elif add_selectbox2 == 'Gamma Distribution':
                alpha = st.slider('Shape Parameter (α)', 0.1, 10.0, 1.0)
                beta = st.slider('Scale Parameter (β)', 0.1, 2.0, 1.0)
                
            elif add_selectbox2 == 'Erlang Distribution':
                k = st.slider('Stage Parameter (k)', 1, 10, 1)
                mu = st.slider('Average (μ)', 0.1, 10.0, 1.0)
        
        
    if add_selectbox1 == 'Discrete Distributions':

        st.header('Discrete Distributions')

        match add_selectbox2:
            case 'Benford Distribution':
                benford()
            case 'Bernoulli Distribution':
                bernoulli(p)
            case 'Beta-Binomial Distribution':
                beta_binomial(a, b, n)
            case 'Poisson Distribution':
                poisson(t, llambda)
            
    elif add_selectbox1 == 'Continuous Distributions':
        
        st.header('Continuous Distributions')
        
        match add_selectbox2:
            case 'Arcsin Distribution':
                arcsin()
            case 'Beta Distribution':
                beta_distribution(a, b)
            case 'Arctangent Distribution':
                artangent(llambda, theta)
            case 'Cauchy Distribution':
                cauchy(x0, gamma)
            case 'Chi Distribution':
                chi(n)
            case 'Chi-square Distribution':
                chi_square(n)
            case 'Erlang Distribution':
                erlang(k, mu)
            case 'Gamma Distribution':
                gamma(alpha, beta)
        
