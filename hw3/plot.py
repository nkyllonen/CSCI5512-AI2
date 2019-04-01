'''
CSCI 5512 - AI 2 - HW 3
Nikki Kyllonen
kyllo089
'''

import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

def plot2():
    # 1 - low, 2 - med, 3 - high
    x = [1, 2, 3]
    f1 = [0.3045, 0.5243, 0.1713]
    f2 = [0.3003, 0.5395, 0.1383]
    f3 = [0, 0.2466, 0.7534]
    s1 = [0.2190, 0.5568, 0.2241]
    s2 = [0.1179, 0.5787, 0.3034]
    plt.plot(x, f1, 'r--', x, f2, 'g-+', x, f3, 'b-*',
            x, s1, 'r-+', x, s2, 'g--')

    plt.xlabel('(1) x = low, (2) x = med, (3) x = high')
    plt.ylabel('Probability of (x)')
    plt.title('Filtering and Smoothing Probabilities')
    plt.grid(True)
    plt.legend(['P(x1|e1)', 'P(x2|e1:2)', 'P(x3|e1:3)',
            'P(x1|e1:3)', 'P(x2|e1:3)'])

    plt.show()

'''
plot_normal:
    https://emredjan.github.io/blog/2017/07/19/plotting-distributions/
'''
def plot_normal(x_range, mu=0, sigma=1, cdf=False, **kwargs):
    '''
    Plots the normal distribution function for a given x range
    If mu and sigma are not provided, standard normal is plotted
    If cdf=True cumulative distribution is plotted
    Passes any keyword arguments to matplotlib plot function
    '''
    x = x_range
    if cdf:
        y = ss.norm.cdf(x, mu, sigma)
    else:
        y = ss.norm.pdf(x, mu, sigma)
    plt.plot(x, y, **kwargs)
