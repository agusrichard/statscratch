from ..utils import multi_combination

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