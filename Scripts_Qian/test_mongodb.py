#!/usr/bin/python

from pymongo import MongoClient

client=MongoClient()
client=MongoClient('localhost',27017)
db=client.test

db.dvds.insert({'title': "The Hitchhikers Guide to the Galaxy",
                   'episodes': [{'title': "Episode 1", 'desc': "..."},
                                {'title': "Episode 2", 'desc': "..."},
                                {'title': "Episode 3", 'desc': "..."},
                                {'title': "Episode 4", 'desc': "..."},
                                {'title': "Episode 5", 'desc': "..."},
                                {'title': "Episode 6", 'desc': "..."}]})

episode = db['dvds'].find_one({'episodes.title': "Episode 1"})
print(list(db.dvds.aggregate([
  {"$unwind": "$episodes"}, # One document per episode
  {"$match": {"episodes.title": "Episode 1"} }, # Selects (filters)
  {"$group": {"_id": "$_id", # Put documents together again
              "episodes": {"$push": "$episodes"},
              "title": {"$first": "$title"} # Just take any title
             }
  },
  {"$project":{"_id":0,"episodes":"$episodes","title":"$title"}}
])))
print("\n")
print(list(db.dvds.find_one({'episodes.title':'Episode 1'},{'episodes.title':1})))
