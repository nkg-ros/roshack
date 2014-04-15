import png


SIZE = 256


def list_to_grid(data, size=None):
    if size is None:
        size = SIZE
    return _chunks(data, size)


def grid_to_list(data):
    result = []
    for sublist in data:
        result = result + sublist

    return result


def _chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
