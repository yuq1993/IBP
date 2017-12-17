#!/usr/bin/python

# data source: https://www.rcsb.org/pdb/browse/homo_sapiens.do
# download Json file and store them in mongodb
import json

from pymongo import MongoClient
client=MongoClient()
client=MongoClient('localhost',27017)
db=client.gene2pdb_database
all_data=db.all_data
with open('../data/homo_sapiens_download.jsp.html') as json_data:
    d = json.load(json_data)
    all_data.insert(d)
print(db.all_data.find_one())
    
