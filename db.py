from pymongo import MongoClient

#CONNECTION = (
#    'mongodb://dc10.galv.in/ros'
#)
CONNECTION = (
    'mongodb://mongoukhack2:ohjuxief2Xee@lon-c9-0.objectrocket.com:43034/ros'
)

client = MongoClient(CONNECTION)
db = client['ros']


tiles = db['tiles']
tiles_meta = db['tiles_meta']

def get_tile_data(x, y, z):
    tile = tiles.find_one(
        {'_id': {'x': x, 'y': y, 'z': z}}
    )
    return tile
