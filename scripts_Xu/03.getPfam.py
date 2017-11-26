# get protein domain info and write in the result_Pfam.txt
# required: UniprotKBonly(in uniprotkb-files folder), uniprot_pfam.txt(03.getPfam.sh), PDBuniprot
# TODO: rethink if all the pfam domains need to be stored or only domian that contains mutation

import sys
import re
from collections import defaultdict

uniprot_file = open("UniprotKBonly",'r')
PDBUniprot_file = open("PDBuniprot",'r')
uniprotPfam_file = open("uniprot_pfam.txt",'r')

table=open("result_Pfam.txt",'w')

uniprot_IDs = uniprot_file.readlines()
uniprotPfam = uniprotPfam_file.readlines()

uniprot_dic={}
for id in uniprot_IDs:
    id=id.strip()
    uniprot_dic[id]=0

#write pfam result in uniprot_dic
for line in uniprotPfam:
    line = line.strip()
    if line != "":
        WT_ID = line.split("|")[1]
        pattern=re.compile(r'\s\w+\s')
        info = pattern.findall(line)
        uniprot_dic[WT_ID] = info[2].strip() + '\t' + info[3].strip() + '\t' + info[4].strip() + '\t' + info[5].strip()

#write pfam result in table
table.write("PDB\tuniprot\tstart\tend\tpfam\n")
for line in PDBUniprot_IDs:
    line=line.strip()
    PDB_ID = line.split('\t')[0]
    uniprot_ID = line.split('\t')[1]
    uniprot_pfam = uniprot_dic.get(uniprot_ID)
    newline = line + '\t' + uniprot_pfam + '\n'
    table.write(newline)

uniprot_file.close()
uniprotPfam_file.close()
PDBUniprot_file.close()
table.close()

