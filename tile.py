import png


SIZE = 256


def list_to_grid(data, size=None):
    if size is None:
        size = SIZE
    return _chunks(data, size)


def _chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
