from pymongo import MongoClient

CONNECTION = (
    'mongodb://mongoukhack2:ohjuxief2Xee@lon-c9-0.objectrocket.com:43034/ros'
)


client = MongoClient(CONNECTION)
db = client['ros']

tiles = db['tiles']
tiles_meta = db['tiles_meta']



