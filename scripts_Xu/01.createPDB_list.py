# input: new_info_fromSNPeff.target.pdb_and_residue.txt(from Qian's script)
# output: each line is the pdb info needed for foldx

import subprocess,re

subprocess.call('grep PASS ../result/new_info_fromSNPeff.target.pdb_and_residue.txt > Snp_PDB_info.txt', shell=True)

snp_PDB_file = open('Snp_PDB_info.txt','r')
PDB_list_file = open('individual_list.txt','w')

line = snp_PDB_file.readline()
while line != '':
    info = line.split('\t')
    pdb_info = re.findall("\w+",info[12])
    PDBid = pdb_info[0] #no .pdb suffix
    chain = pdb_info[2]
    pos = pdb_info[3]
    ref = pdb_info[6]
    alt = info[13].strip()[0]
    chr = info[0]
    g_pos = info[1]
    ENST = info[9]
    newline = chr + '\t' + g_pos + '\t' + ENST + '\t' + PDBid + '\t' + ref + '\t' + chain + '\t' + pos + '\t' + alt + '\n'
    PDB_list_file.write(newline)
    line = snp_PDB_file.readline()

snp_PDB_file.close()
PDB_list_file.close()
