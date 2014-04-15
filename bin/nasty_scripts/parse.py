import csv

from roshack.bin.nasty_scripts import scale
from roshack.bin.nasty_scripts.mongo import db


a = [90, -180]
b = [-90, 180]

t = scale.project_to_square(a, b, 256 * 32)

coll = db['raw_points']


count = 0
with open('data/allCountries.txt', 'r') as fh:

    read = csv.reader(fh, delimiter="\t")

    while True:
        try:
            row = read.next()

            if count % 10000 == 0:
                print count

            lat_long = [float(i) for i in row[4:6]]

            grid = [int(i) for i in t.map_to(lat_long)]
            doc = {
                'lat_long': lat_long,
                #'grid': grid,
                'grid_x': grid[0],
                'grid_y': grid[1],
                'grid': grid,
                'tile_x': int(grid[0]/256),
                'tile_y': int(grid[1]/256),
                'tile_z': 5,
            }

            coll.save(doc)
            count += 1
        except Exception, e:
            print "Oh dear", e
            continue

