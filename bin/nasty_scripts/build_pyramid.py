import numpy as np
import math

from roshack.bin.nasty_scripts.mongo import db

coll = db['tiles']


def generate_tile(level, x, y):
    print level, x, y

    ids = [
        {
            'x': 2*x + x_mod,
            'y': 2*y + y_mod,
            'z': level + 1,
        } for x_mod in range(2) for y_mod in range(2)]

    docs = coll.find({'_id': {'$in': ids}})

    final = np.zeros((256, 256))

    for doc in docs:
        tx, ty = doc['_id']['x'], doc['_id']['y']
        off_x = (tx % 2) * 128
        off_y = (ty % 2) * 128

        tile_array = np.array(doc['values'])
        tile_array.shape = (256,256)

        smaller = reduce_128(tile_array)

        final[
                off_x:off_x + 128,
                off_y:off_y + 128] = smaller

    final.shape = (1, 256*256)

    final_doc = {
        '_id': {
            'x': x,
            'y': y,
            'z': level,
        },
        'values': list(final[0])
    }

    coll.save(final_doc)


def reduce_128(np_array):
    out = np.zeros((128, 128))

    for x_off in range(2):
        for y_off in range(2):
            out += np_array[x_off::2, y_off::2]

    return out


def generate_level(level):
    sq_size = int(math.pow(2, level))

    for xy in ((x,y) for x in range(sq_size) for y in range(sq_size)):
        generate_tile(level, xy[0], xy[1])

print "Level 4"
generate_level(4)
print "Level 3"
generate_level(3)
print "Level 2"
generate_level(2)
print "Level 1"
generate_level(1)
print "Level 0"
generate_level(0)