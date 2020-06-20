import functools

def factorial(x, recursive=False):
    """
    Calculate factorial of x (x!) iteratively or recursively.

    Parameters
    ----------
    x : int
        Value for factorial... x!
    recursive : bool, default False
        If True, the calculation using recursion, else using iteration
    """
    if x < 0:
        raise ValueError('x can not negative')
    elif type(x) == float:
        raise TypeError('x must be an integer')
    elif x == 0:
        return 1
    else:
        if recursive:
            if x == 1:
                return x
            else:
                return x * factorial(x - 1)
        else:
            mult = 1
            for i in range(1, x + 1):
                mult *= i
            return mult


def combination(n, x, **factorial_kwargs):
    """
    Calculate C(n, x)

    Parameters
    ----------
    n : int
        Total number of items
    x : int
        Total number of items chosen
    **factorial_kwargs : bool, default False
        True, use recursion. False, use iteration
    """
    if type(n) != int and type(x) != int:
        raise TypeError('n and x must be integers')
    elif x > n:
        raise ValueError('x can not larger than n')
    else:
        return int(factorial(n, **factorial_kwargs) / (factorial(n-x, **factorial_kwargs) * factorial(x, **factorial_kwargs)))


def multi_combination(n, *xs, **factorial_kwargs):
    """
    Calculate C(n, (x1, x2, x3, ..., xk))

    Parameters
    ----------
    n : int
        The total number of trials
    *xs : list of ints
        The number of successes for each kind. 
    **factorial_kwargs
        keyword arguments for factorial

    """
    if type(n) != int:
        raise TypeError('n must be an integer')
    else:
        xs = [1] + list(xs)
        print(xs)
        denominator = functools.reduce(lambda prev, curr: prev * factorial(curr, **factorial_kwargs), xs)
        print(denominator)
        print(factorial(n))
        return int(factorial(n, **factorial_kwargs) / denominator)