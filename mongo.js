#!/usr/bin/env node
//load the Client interface
var MongoClient = require('mongodb').MongoClient;
var connection_string ='mongoukhack2:ohjuxief2Xee@lon-c9-0.objectrocket.com:43034/ros?w=1'
// the client db connection scope is wrapped in a callback:
MongoClient.connect('mongodb://'+connection_string, function(err, db) {
  if(err) throw err;
  var collection = db.collection('raw_points').find().limit(10).toArray(function(err, docs) {
    console.dir(docs);
    db.close();
  })
})
