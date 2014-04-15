from pymongo import MongoClient

CONNECTION = (
   'mongodb://mongoukhack2:ohjuxief2Xee@lon-c9-0.objectrocket.com:43034/ros'
)
CONNECTION = (
    'mongodb://localhost'
)

client = MongoClient(CONNECTION)
db = client['ros']


