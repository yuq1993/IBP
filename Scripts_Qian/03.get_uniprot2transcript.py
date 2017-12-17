#!/usr/bin/python

# 这个脚本使用uniprot获得对应的pdb 列表 以及transcriptID

infile=open('info_fromSNPeff.target.uniprot.txt','r')
dataset=open('../data/HUMAN_9606_idmapping_selected.tab','r')
pdb={}
gene={}
transcripts={}
for line in dataset:
    data=line.split("\t")
    pdb[data[0]]=data[5]
    transcripts[data[0]]=data[19]
    gene[data[0]]=data[18]

for line in infile:
    data=line.split("\t")
    if(len(data)<12): # Becuase some lines only have ENSG no ENST
        print(line.strip())
    else:
        tmp=data[11].replace(" ","")
    if("NA" in tmp or line[0:5]=="chrom"):
        print(line.strip())
    else:
        if("N" in data[13]): # if no pdb, then do not consider it
            print(line.strip())
        else:
            UniprotID=data[15].replace(" ","")
            print(line.strip(),"\t","|||","\t",gene[UniprotID],"\t",transcripts[UniprotID],"\t",pdb[UniprotID])

