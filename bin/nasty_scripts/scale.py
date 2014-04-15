

def project_to_square(min_v, max_v, square):
    width = max_v[0] - min_v[0]
    height = max_v[1] - min_v[1]

    square = float(square)

    return Transform([-min_v[0], -min_v[1]], [square / width, square / height])


class Transform(object):
    offset = None
    scale = None

    def __init__(self, offset, scale):
        self.offset = offset
        self.scale = scale

    def map_to(self, xy):
        return [
            (xy[0] + self.offset[0]) * self.scale[0],
            (xy[1] + self.offset[1]) * self.scale[1]
        ]


t = project_to_square([-180, 90], [180, -90], 8192)

print t.map_to([180, -90])