# get protein domain info and write in the result_Pfam.txt
# required: UniprotKBonly(in uniprotkb-files folder), uniprot_pfam.txt(03.getPfam.sh), PDBuniprot
# TODO: rethink if all the pfam domains need to be stored or only domian that contains mutation

import sys
import re
from collections import defaultdict

uniprot_file = open("uniprotID.txt",'r')
#PDBUniprot_file = open("PDBuniprot",'r')
#uniprotPfam_file = open("pfam_result.txt",'r')
uniprotPfam_file = open("pfam_ENST_result.txt",'r')

table=open("pfam_ENST_table.txt",'w')

uniprot_IDs = uniprot_file.readlines()
uniprotPfam = uniprotPfam_file.readlines()

uniprot_dic=defaultdict(list)
for id in uniprot_IDs:
    id=id.strip()
    uniprot_dic[id].append(0)

#write pfam result in uniprot_dic
for line in uniprotPfam:
    line = line.strip()
    if line != "":
        WT_ID = line.split("|")[1]
        info = re.split("\s+",line)
        newline = info[3] + '\t' + info[4] + '\t' + info[6] + '\t' + info[7]
        uniprot_dic[WT_ID].append(newline)

#write pfam result in table
table.write("uniprot\tstart\tend\tpfam_name\tfamily\n")
for line in uniprot_IDs:
    line=line.strip()
    domain_info = uniprot_dic.get(line)
    if len(domain_info) >1:
        for i in range(1,len(domain_info)):
            newline = line + '\t' + domain_info[i] + '\n'
            table.write(newline)

uniprot_file.close()
uniprotPfam_file.close()
#PDBUniprot_file.close()
table.close()

