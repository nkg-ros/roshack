import numpy as np

from roshack.bin.nasty_scripts.mongo import db

coll = db['raw_points']

coll.ensure_index([('tile_x', 1), ('tile_y', 1)])

print "index done"

doc = coll.aggregate([
    {"$group": {
        "_id": {
            "x": "$tile_x",
            "y": "$tile_y",
            "z": "$tile_z",
        },
    }},
])

print "Agg done"

total = len(doc['result'])
count = 0
save_coll = db['tiles']

for tile in doc['result']:
    count += 1
    a = np.zeros((256,256))
    tile_x = tile['_id']['x']
    tile_y = tile['_id']['y']

    print "Tile: ", count, total, tile_x, tile_y

    xoff = 256 * tile_x
    yoff = 256 * tile_y


    for point in coll.find({
        "tile_x": tile_x,
        "tile_y": tile_y
    }):

        (px, py) = point['grid_x'], point['grid_y']
        a[px - xoff][py - yoff] += 1

    a.shape = (1, 256*256)

    flat = list(a[0])

    to_save = {
        '_id': tile['_id'],
        'values': flat,
    }

    save_coll.save(to_save)
