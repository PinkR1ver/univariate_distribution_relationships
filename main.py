import streamlit as st
from distribution.distribution import *  
    
      
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
                n = st.slider('Number of Trials (n)', 2, 40, 5)
                
            elif add_selectbox2 == 'Poisson Distribution':
                llambda = st.slider('Rate Parameter (λ)', 0.1, 10.0, 1.0)
                t = st.slider('Time Interval (t)', 0.1, 10.0, 1.0)
                k = st.slider('X-axis, Number of Events (k)', 2, 80, 2)
            
        elif add_selectbox1 == 'Continuous Distributions':
            add_selectbox2 = st.selectbox(
                'Select a Distribution',
                ('Arcsin Distribution', 'Arctangent Distribution', 'Beta Distribution', 
                 'Cauchy Distribution', 'Chi Distribution', 'Chi-square Distribution', 
                 'Erlang Distribution', 'Exponential Distribution', 'Exponential Power Distribution',
                 'Gamma Distribution', 'Student\'s t Distribution')
            )
            
            if add_selectbox2 == 'Beta Distribution':
                a = st.slider('Shape Parameter (a)', 0.1, 100.0, 1.0)
                b = st.slider('Shape Parameter (b)', 0.1, 100.0, 1.0)
                
            elif add_selectbox2 == 'Arctangent Distribution':
                llambda = st.slider('Shape Parameter (λ)', 0.1, 10.0, 1.0)
                theta = st.slider('Shape Parameter (θ)', 0.1, 10.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
            elif add_selectbox2 == 'Cauchy Distribution':
                x0 = st.slider('Location Parameter (x0)', -10.0, 10.0, 0.0)
                gamma = st.slider('Scale Parameter (γ)', 0.1, 10.0, 1.0)
                x_left_range = st.slider('X-axis Negative Range', -100.0, -1.0, -10.0)
                x_right_range = st.slider('X-axis Positive Range', 1.0, 100.0, 10.0)
                
            elif add_selectbox2 == 'Chi Distribution':
                n = st.slider('Degrees of Freedom (n)', 1, 100, 1)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
            
            elif add_selectbox2 == 'Chi-square Distribution':
                n = st.slider('Degrees of Freedom (n)', 1, 10, 1)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
            elif add_selectbox2 == 'Erlang Distribution':
                k = st.slider('Stage Parameter (k)', 1, 10, 1)
                mu = st.slider('Average (μ)', 0.1, 10.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
            elif add_selectbox2 == 'Exponential Distribution':
                llambda = st.slider('Rate Parameter (λ)', 0.1, 10.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0) 
            
            elif add_selectbox2 == 'Exponential Power Distribution':
                llambda = st.slider('Rate Parameter (λ)', 0.01, 3.0, 1.0)
                kappa = st.slider('Shape Parameter (κ)', 0.01, 3.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 5.0, 2.0)
            
            elif add_selectbox2 == 'Gamma Distribution':
                alpha = st.slider('Shape Parameter (α)', 0.1, 10.0, 1.0)
                beta = st.slider('Scale Parameter (β)', 0.1, 2.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
            elif add_selectbox2 == 'Student\'s t Distribution':
                nu = st.slider('Degrees of Freedom (ν)', 1.0, 100.0, 1.0)
                x_left_range = st.slider('X-axis Negative Range', -100.0, -1.0, -10.0)
                x_right_range = st.slider('X-axis Positive Range', 1.0, 100.0, 10.0)
        
        
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
                poisson(t, llambda, k)
            
    elif add_selectbox1 == 'Continuous Distributions':
        
        st.header('Continuous Distributions')
        
        match add_selectbox2:
            case 'Arcsin Distribution':
                arcsin()
            case 'Beta Distribution':
                beta_distribution(a, b)
            case 'Arctangent Distribution':
                artangent(llambda, theta, x_range)
            case 'Cauchy Distribution':
                cauchy(x0, gamma, x_left_range, x_right_range)
            case 'Chi Distribution':
                chi(n, x_range)
            case 'Chi-square Distribution':
                chi_square(n, x_range)
            case 'Erlang Distribution':
                erlang(k, mu, x_range)
            case 'Exponential Distribution':
                exponential(llambda, x_range)
            case 'Gamma Distribution':
                gamma(alpha, beta, x_range)
            case 'Student\'s t Distribution':
                student_t(nu, x_left_range, x_right_range)
            case 'Exponential Power Distribution':
                exponential_power(llambda, kappa, x_range)
        
