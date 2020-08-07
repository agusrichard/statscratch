import numpy as np
from ..utils import combination, multi_combination


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


def multinomial_pmf(n, xs, ps, **kwargs):
    """
    Calculate Multinomial Probability Mass Function

    Parameters
    ----------
    n : int
        The total number of Bernoulli Trials
    xs : list
        The list of number of success for each outcomes
    Ps : list
        The list of probabilty of success for each outcomes
    **factorial_kwargs : bool, default False
        Keyword for factorial calculation

    Returns
    -------
    value, mean, std

    value : numeric
        Calculated value
    mean : numeric
        Average
    std : numeric, Standard Deviation
        Standard Deviation
    """

    if (sum(ps) != 1):
        raise ValueError('Sum of ps must equals to one')

    def reduce_multiplication(ps, xs):
        value = 1
        for p, x in zip(ps, xs):
            value *= p ** x
        return value

    left = multi_combination(n, *xs)
    right = reduce_multiplication(ps, xs)
    return left * right


def hypergeometric_pmf(x, N, n, k):
    """
    Calculate Hypergeometric Probability Mass Function

    Parameters
    ----------
    x: int
        Number of successes of n trials
    N: int
        Total number of items
    n: int
        Sample size
    k: int
        Number of items labeled success

    Return
    ------
    Probability of Hypergeometric Distribution
    """
    if (not (type(x) == int and type(N) == int and type(n) == int and type(k) == int)):
        raise TypeError('x, N, n, k must be integers')

    success = combination(k, x)
    fail = combination(N-k, n-x)
    all = combination(N, n)
    return (success * fail) / all