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
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                if st.session_state.get('a_list') is None:
                    st.session_state.a_list = []
                    st.session_state.b_list = []
                
                a = st.slider('Shape Parameter (a)', 0.1, 10.0, 1.0)
                b = st.slider('Shape Parameter (b)', 0.1, 10.0, 1.0)
                n = st.slider('Number of Trials (n)', 2, 40, 5)
                
                a = st.session_state.a_list + [a]
                b = st.session_state.b_list + [b]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.a_list.append(a[-1])
                    st.session_state.b_list.append(b[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
                
                
            elif add_selectbox2 == 'Poisson Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                if st.session_state.get('llambda_list') is None:
                    st.session_state.llambda_list = []
                    st.session_state.t_list = []
                
                llambda = st.slider('Rate Parameter (λ)', 0.1, 10.0, 1.0)
                t = st.slider('Time Interval (t)', 0.1, 10.0, 1.0)
                k = st.slider('X-axis, Number of Events (k)', 2, 80, 2)
                
                llambda = st.session_state.llambda_list + [llambda]
                t = st.session_state.t_list + [t]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.llambda_list.append(llambda[-1])
                    st.session_state.t_list.append(t[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
            
        elif add_selectbox1 == 'Continuous Distributions':
            add_selectbox2 = st.selectbox(
                'Select a Distribution',
                ('Arcsin Distribution', 'Arctangent Distribution', 'Beta Distribution', 
                 'Cauchy Distribution', 'Chi Distribution', 'Chi-square Distribution', 
                 'Erlang Distribution', 'Exponential Distribution', 'Exponential Power Distribution',
                 'Gamma Distribution', 'Gumbel Distribution', 'Student\'s t Distribution'
                )
            )
                
            if add_selectbox2 == 'Arctangent Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                if st.session_state.get('llambda_list') is None:
                    st.session_state.llambda_list = []
                    st.session_state.theta_list = []
                
                llambda = st.slider('Shape Parameter (λ)', 0.1, 10.0, 1.0)
                theta = st.slider('Shape Parameter (θ)', 0.1, 10.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
                llambda = st.session_state.llambda_list + [llambda]
                theta = st.session_state.theta_list + [theta]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.llambda_list.append(llambda[-1])
                    st.session_state.theta_list.append(theta[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                    
            elif add_selectbox2 == 'Beta Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('a_list') is None:
                    st.session_state.a_list = []
                    st.session_state.b_list = []
                
                a = st.slider('Shape Parameter (a)', 0.1, 100.0, 1.0)
                b = st.slider('Shape Parameter (b)', 0.1, 100.0, 1.0)
                
                a = st.session_state.a_list + [a]
                b = st.session_state.b_list + [b]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.a_list.append(a[-1])
                    st.session_state.b_list.append(b[-1])
                
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
            elif add_selectbox2 == 'Cauchy Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('x0_list') is None:
                    st.session_state.x0_list = []
                    st.session_state.gamma_list = []
                
                x0 = st.slider('Location Parameter (x0)', -10.0, 10.0, 0.0)
                gamma = st.slider('Scale Parameter (γ)', 0.1, 10.0, 1.0)
                x_left_range = st.slider('X-axis Negative Range', -100.0, -1.0, -10.0)
                x_right_range = st.slider('X-axis Positive Range', 1.0, 100.0, 10.0)
                
                x0 = st.session_state.x0_list + [x0]
                gamma = st.session_state.gamma_list + [gamma]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.x0_list.append(x0[-1])
                    st.session_state.gamma_list.append(gamma[-1])
                
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
            elif add_selectbox2 == 'Chi Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                if st.session_state.get('n_list') is None:
                    st.session_state.n_list = []
                
                n = st.slider('Degrees of Freedom (n)', 1, 100, 1)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
                n = st.session_state.n_list + [n]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.n_list.append(n[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
            
            elif add_selectbox2 == 'Chi-square Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('n_list') is None:
                    st.session_state.n_list = []
                
                n = st.slider('Degrees of Freedom (n)', 1, 10, 1)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
                n = st.session_state.n_list + [n]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.n_list.append(n[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
            elif add_selectbox2 == 'Erlang Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('k_list') is None:
                    st.session_state.k_list = []
                    st.session_state.mu_list = []
                
                k = st.slider('Stage Parameter (k)', 1, 10, 1)
                mu = st.slider('Average (μ)', 0.1, 10.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
                k = st.session_state.k_list + [k]
                mu = st.session_state.mu_list + [mu]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.k_list.append(k[-1])
                    st.session_state.mu_list.append(mu[-1])
                
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
            elif add_selectbox2 == 'Exponential Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('llambda_list') is None:
                    st.session_state.llambda_list = []
                
                llambda = st.slider('Rate Parameter (λ)', 0.1, 10.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
                llambda = st.session_state.llambda_list + [llambda]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.llambda_list.append(llambda[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
            
            elif add_selectbox2 == 'Exponential Power Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('llambda_list') is None:
                    st.session_state.llambda_list = []
                    st.session_state.kappa_list = []
                
                llambda = st.slider('Rate Parameter (λ)', 0.01, 3.0, 1.0)
                kappa = st.slider('Shape Parameter (κ)', 0.01, 3.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 5.0, 2.0)
                
                llambda = st.session_state.llambda_list + [llambda]
                kappa = st.session_state.kappa_list + [kappa]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.llambda_list.append(llambda[-1])
                    st.session_state.kappa_list.append(kappa[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
            
            elif add_selectbox2 == 'Gamma Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('alpha_list') is None:
                    st.session_state.alpha_list = []
                    st.session_state.beta_list = []
                
                alpha = st.slider('Shape Parameter (α)', 0.1, 10.0, 1.0)
                beta = st.slider('Scale Parameter (β)', 0.1, 2.0, 1.0)
                x_range = st.slider('X-axis Range', 1.0, 100.0, 10.0)
                
                alpha = st.session_state.alpha_list + [alpha]
                beta = st.session_state.beta_list + [beta]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.alpha_list.append(alpha[-1])
                    st.session_state.beta_list.append(beta[-1])
                    
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
            elif add_selectbox2 == 'Gumbel Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('mu_list') is None:
                    st.session_state.mu_list = []
                    st.session_state.beta_list = []
                
                mu = st.slider('Location Parameter (μ)', -10.0, 10.0, 0.0)
                beta = st.slider('Scale Parameter (β)', 0.1, 10.0, 1.0)
                x_left_range = st.slider('X-axis Negative Range', -100.0, -1.0, -10.0)
                x_right_range = st.slider('X-axis Positive Range', 1.0, 100.0, 10.0)
                
                mu = st.session_state.mu_list + [mu]
                beta = st.session_state.beta_list + [beta]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.mu_list.append(mu[-1])
                    st.session_state.beta_list.append(beta[-1])

                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
                
            elif add_selectbox2 == 'Student\'s t Distribution':
                
                if st.session_state.get('flag') is None:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                
                elif st.session_state.flag != add_selectbox2:
                    st.session_state.clear()
                    st.session_state.flag = add_selectbox2
                    
                if st.session_state.get('nu_list') is None:
                    st.session_state.nu_list = []
                
                nu = st.slider('Degrees of Freedom (ν)', 1.0, 100.0, 1.0)
                x_left_range = st.slider('X-axis Negative Range', -100.0, -1.0, -10.0)
                x_right_range = st.slider('X-axis Positive Range', 1.0, 100.0, 10.0)
                
                nu = st.session_state.nu_list + [nu]
                
                anchor = st.button('Anchor', type='primary')
                if anchor:
                    st.session_state.nu_list.append(nu[-1])
                
                reset = st.button('Reset', type='primary')
                if reset:
                    st.session_state.clear()
                    st.rerun()
        
        
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
            case 'Gumbel Distribution':
                gumbel(mu, beta, x_left_range, x_right_range)
            case 'Student\'s t Distribution':
                student_t(nu, x_left_range, x_right_range)
            case 'Exponential Power Distribution':
                exponential_power(llambda, kappa, x_range)
        
