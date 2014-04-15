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


def render_image(data_list):
    """
    Render a 2D array of data as a 256x256 PNG
    """
    pixel_list = map(value_to_pixel, data_list)

    # convert list to grid
    image = Image.new(mode='L', size=(256,256))
    image.putdata(np.array(pixel_list))

    return image


def value_to_pixel(value):
    """
    Turn a numerical value into a pixel array
    ex: 12 -> [255, 255, 255]
    """
    if value == 0:
        return 0
    else:
        return 255


def _chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def _curve(val, m):
    return math.pow(
        math.log(val) / math.log(m),
        1.5
    )
