from math import tan, pi


def polysum(n, s):
    """

    :param n:number of sides
    :param s: side length
    :return: area + perimeter**2 (rounded 4 decimal)
    """
    areapoly = (0.25 * n * s ** 2) / (tan(pi / n))
    perimeterpoly = n * s
    return round(areapoly + perimeterpoly ** 2, 4)
