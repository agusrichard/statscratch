from ..utils import combination

def binomial_pmf(x, n, p, bootstrap=False):
    """
        
    """

    if type(x) != int and type(n) != int and type(p) != float:
        raise TypeError('x and n must be integers, and p must be a float')
    elif p < 0 and p > 1:
        raise ValueError('p must between 0 and 1, inclusive')
    else:
        return combination(n, x) * (p ** x) * ((1 - p) ** (n - x))