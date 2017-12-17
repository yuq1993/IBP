#!usr/bin/python

# 从mongodb中根据ENSG得到各种信息

infile=open('info_fromSNPeff.target.txt','r')

import sys

from pymongo import MongoClient
client=MongoClient()
client=MongoClient('localhost',27017)
db=client.gene2pdb_database
all_data=db.all_data

queryID=""
flag=1
print("chrom\tlocation\trefSNP\taltSNP\tQUAL\tDP\tSequence_Ontology_term\tImpact\tENSG\tENST\tId\tGeneSymbol\tHasPDB\tName\tUniProt\tLocus\tRefseq\tEnsembl")
for line in infile:
    data=line.split()
    if(data[8] == "ENSG"):
        continue
    if(data[8] != queryID):
        queryID=data[8] # ENSG
        #print(queryID)
        result_cursor=db.all_data.aggregate([{"$unwind":"$rows"},{"$match":{"rows.cell":queryID}}])
        tmp=list(result_cursor)
        if(tmp==[]):
            print(line.strip(),"\t","|||","\t","NA")
            flag=0
            continue
        flag=1
        result_dict=tmp[0]
        info_list=result_dict['rows']['cell']
        if(info_list[2]=="*"):
            HasPDB="Y"
        else:
            HasPDB="N"
        print(line.strip(),"\t","|||","\t",info_list[0],"\t",info_list[1],"\t",HasPDB,"\t",info_list[3],"\t",info_list[4],"\t",info_list[5],"\t",info_list[6],"\t",info_list[7])
        Id=info_list[0]
        GeneSymbol=info_list[1]
        Name=info_list[3]
        UniProt=info_list[4]
        Locus=info_list[5]
        Refseq=info_list[6]
        Ensembl=info_list[7]
    else:
        if(flag==0):
            print(line.strip(),"\t","|||","\t","NA")
        else:
            print(line.strip(),"\t","|||","\t",info_list[0],"\t",info_list[1],"\t",HasPDB+"\t",info_list[3],"\t",info_list[4],"\t",info_list[5],"\t",info_list[6],"\t",info_list[7])


    
    

