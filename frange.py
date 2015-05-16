def frange(start, stop, step):
    """
    This function is not my personnal work.
    http://www.pythoncentral.io/pythons-range-function-explained/
    But it might be helpfull
    """
    i = start
    while i < stop:
        yield i
        i += step
