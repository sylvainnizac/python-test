__author__ = 'Sylvain Nizac'

from math import sqrt

def euclidean_norm (nbr1, nbr2):
    """
    starting for a value or the coordinates of a point (2D, 3D, ...) calculates the norm of resulting vector.
    this function accept any length of tuple/list
    if the input is incorrect an error is raised, you have to catch it!
    :param nb1: int, tuple or list contains de values to be normed
    :param nb2: int, tuple or list contains de values to be normed
    :return: the normed value
    """
    if isinstance(nbr1, (int, )) & isinstance(nbr2, (int, )):
        if nbr1 == nbr2:
            res = 0
        else:
            res = sqrt(nbr1**2 + nbr2**2)

    elif isinstance(nbr1, (tuple, list)) & isinstance(nbr2, (tuple, list)):
        if len(nbr1) == len(nbr2) & len(nbr1) != 0:
            res = 0
            for nb1 in nbr1:
                for nb2 in nbr2:
                    temp = (nb2 - nb1)**2
                    res += temp
            res = sqrt(res)
        else:
            raise MyInputError('Input List or tuples have different length or are empty!')

    else:
        raise MyInputError('Input are not ints, tuples or lists !')

    return res


class MyInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
