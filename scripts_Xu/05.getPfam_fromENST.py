# get protein domain info and write in the pfam_ENST_table.txt
# required: pfam_ENST_result.txt(from 04.getPfam_fromENST.sh)
# TODO: rethink if all the pfam domains need to be stored or only domian that contains mutation

import sys
import re
from collections import defaultdict

Pfam_file = open("pfam_ENST_result.txt",'r')
ENST_file = open("ENSTid.txt",'r')

table=open("../result/pfam_ENST_table.txt",'w')

ENST_IDs = ENST_file.readlines()
ENST_Pfam = Pfam_file.readlines()

ENST_dic=defaultdict(list)
for id in ENST_IDs:
    id=id.strip()
    ENST_dic[id].append(0)

#write pfam result in ENST_dic
for line in ENST_Pfam:
    line = line.strip()
    if line != "":
        info = re.split("\s+",line)
        ENSTid = info[0]
        newline = info[3] + '\t' + info[4] + '\t' + info[6] + '\t' + info[7]
        ENST_dic[ENSTid].append(newline)

#write pfam result in table.txt
#table.write("ENST\tstart\tend\tpfam_name\tfamily\n")
for line in ENST_IDs:
    line=line.strip()
    domain_info = ENST_dic.get(line)
    if len(domain_info) >1:
        for i in range(1,len(domain_info)):
            newline = line + '\t' + domain_info[i] + '\n'
            table.write(newline)

ENST_file.close()
Pfam_file.close()
table.close()


