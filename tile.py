from PIL import Image
import numpy as np
import math


SIZE = 256


def list_to_grid(data, size=None):
    if size is None:
        size = SIZE
    return list(_chunks(data, size))


def grid_to_list(data):
    result = []
    for sublist in data:
        result = result + sublist

    return result


def render_image(data_list, m):
    """
    Render a 2D array of data as a 256x256 PNG
    """

    # convert list to grid
    image = Image.new(mode='L', size=(256,256))

    li = curve(np.array(data_list), m)

    image.putdata(li)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    return image


def _chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def curve(a, m):
    return np.power(
        np.log(a + 1) / np.log(m + 1),
        1.5
    ) * 255
