#get foldx DDG info and write in the result_DDG.txt
#required: DDG_fxout(from 02.getFoldx_DDG.sh), PDBonly(in pdb-files folder), PDBuniprot.txt,

import sys
import re
from collections import defaultdict


#need have following result file in the same folder.
DDG_fxout = open("DDG_fxout",'r')
PDB_file = open("./pdb-files/PDBonly",'r')
PDBUniprot_file = open("PDBuniprot",'r')

table=open("result_DDG.txt",'w')

#fx_lines = ST_fxout.readlines()
fx_lines = DDG_fxout.readlines()
PDB_IDs = PDB_file.readlines()

PDBUniprot_IDs = PDBUniprot_file.readlines()

PDB_dic=defaultdict(list)
for id in PDB_IDs:
    id=id.strip()
    PDB_dic[id].append(0)

#write DDG with corresponding pdb in PDB_dic
for line in fx_lines:
    pdb_ID = line.split("_")[0]
    pdb_DDG = line.split("\t")[1]
    PDB_dic[pdb_ID].append(pdb_DDG)

#write DG with corresponding pdb in PDB_dic
#for line in fx_lines:
#    pdb_WT_ID=re.split('\t|\./',line)[1].split('.')[0]
#    pdb_WT_DG=line.split('\t')[1]
#    PDB_dic[pdb_WT_ID] = pdb_WT_DG

#write foldx result in table
table.write("PDB\tuniprot\tDDG\n")
for line in PDBUniprot_IDs:
    line=line.strip()
    PDB_ID = line.split('\t')[0]
    PDB_DDG = PDB_dic.get(PDB_ID)
    uniprot_ID = line.split('\t')[1]
    if len(PDB_DDG) > 1:
        for i in range(1,len(PDB_DDG)):
            newline = line + '\t' + PDB_DDG[i] + '\n'
            table.write(newline)

ST_fxout.close()
PDB_file.close()
PDBUniprot_file.close()
table.close()

