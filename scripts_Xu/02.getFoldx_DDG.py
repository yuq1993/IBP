#get foldx DDG info and write in the result_DDG.txt
#required: DDG_fxout.txt(from 02.getFoldx_DDG.sh), MT_list(from 01.create_PDBlist.py)

import sys
import re
from collections import defaultdict


#need have following result file in the same folder.
DDG_fxout = open("./pdb-files/DDG_fxout.txt",'r')
MT_list = open('./pdb-files/individual_list.txt','r')

table=open("../result/result_DDG.txt",'w')

fx_line = DDG_fxout.readline()
list_lines = MT_list.readlines()

PDB_dic=defaultdict(list)
while fx_line != '':
    PDBid = re.findall('[A-Za-z]+_\d+',fx_line)[0]
    PDB_dic[PDBid].append(fx_line.split('\t')[1])
    fx_line = DDG_fxout.readline()

#write DDG in the table_result
for line in list_lines:
    line = line.strip()
    PDBid = line.split('\t')[3]
    DDG_info = PDB_dic.get(PDBid)
    DDG = DDG_info[0]
    if len(DDG_info) > 1:
        del DDG_info[0]
    newline = line + '\t' + DDG + '\n'
    table.write(newline)

#write DDG with corresponding pdb in PDB_dic
'''for line in fx_lines:
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
            table.write(newline)'''

DDG_fxout.close()
MT_list.close()
table.close()
