import numpy as np
from ..utils import combination

def binomial_pmf(x, n, p, **factorial_kwargs):
    """
    Calculate Binomial Probability Mass Function

    Parameters
    ----------
    x : int
        The Number of successes
    n : int
        The total number of Bernoulli Trials
    P : float
        Probability for Bernoulli Trial
    **factorial_kwargs : bool, default False
        Keyword for factorial calculation

    Returns
    -------
    pmf, mean, std

    pmf : numeric
        Probability Mass Function
    mean : numeric
    std : numeric, Standard Deviation
    """

    if type(x) != int and type(n) != int and type(p) != float:
        raise TypeError('x and n must be integers, and p must be a float')
    elif p < 0 and p > 1:
        raise ValueError('p must between 0 and 1, inclusive')
    elif x > n:
        raise ValueError('x can not larger than n')
    else:
        calculated = combination(n, x, **factorial_kwargs) * (p ** x) * ((1 - p) ** (n - x))
        mean = n * p
        std = np.sqrt(mean * (1 - p))
        return calculated, mean, std


def binomial_cmf(n, p, **factorial_kwargs):
    """
    Calculate Binomial Cummulative Probability Mass Function

    Parameters
    ----------
    x : int
        The Number of successes
    n : int
        The total number of Bernoulli Trials
    P : float
        Probability for Bernoulli Trial
    **factorial_kwargs : bool, default False
        Keyword for factorial calculation
    """
    sums = np.array([binomial_pmf(i, n, p)[0] for i in range(0, n + 1)])
    csum = sums.cumsum()
    return sums, csum, csum[-1]