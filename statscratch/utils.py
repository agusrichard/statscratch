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
    if x < 1:
        raise ValueError('x can not negative')
    elif type(x) == float:
        raise TypeError('x must be an integer')
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


def combination(n, x, recursive=False):
    """
    Calculate C(n, x)

    Parameters
    ----------
    n : int
        Total number of items
    x : int
        Total number of items chosen
    recursive : bool, default False
        True, use recursion. False, use iteration
    """
    if type(n) != int and type(x) != int:
        raise TypeError('n and x must be integers')
    else:
        return int(factorial(n, recursive=recursive) / (factorial(n-x, recursive=recursive) * factorial(x, recursive=recursive)))