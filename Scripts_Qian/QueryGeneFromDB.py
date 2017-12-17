#!/usr/bin/python

# 这个脚本是用来从pdb database里面 根据geneID 提取信息的
import sys

queryID=sys.argv[1]


from pymongo import MongoClient
client=MongoClient()
client=MongoClient('localhost',27017)
db=client.gene2pdb_database
all_data=db.all_data

#geneID="ENSG00000131043"
#geneID="ENSG00000224051"
#geneID="ENSG00000187642"



result_cursor=db.all_data.aggregate([{"$unwind":"$rows"},{"$match":{"rows.cell":queryID}}])
tmp=list(result_cursor)
if(tmp==[]):
    print("No result")
    exit()
result_dict=tmp[0]
info_list=result_dict['rows']['cell']
# Id, GeneSymbol, HasPDB, Name, UniProt, Locus, Refseq, Ensembl
print("Id\tGeneSymbol\tHasPDB\tName\tUniProt\tLocus\tRefseq\tEnsembl")
print(info_list[0],info_list[1],info_list[2],info_list[3],info_list[4],info_list[5],info_list[6],info_list[7])
