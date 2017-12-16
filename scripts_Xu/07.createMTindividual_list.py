# To create the individual_list.txt for each PDB with a given file (contains many SNPs in one file, as well as PDBid, position, MTaa, WTaa )
# required file: individual_list.txt(example)

import re
import subprocess
totalMT_file = open("individual_list.txt",'r')

totalMT_list = totalMT_file.readlines()
totalMT_list[8].strip().split('\t')[0]
PDB_ID = totalMT_list[8].strip()
re.findall(r'\w{4}',PDB_ID)
a=totalMT_list[0].replace('^#','')

MT_PDBid = {}
subprocess.call('grep -v "#" ./individual_list.txt | cut -f 4 > MT_PDBonly.txt' ,shell=True)
for line in open('MT_PDBonly.txt'):
    line = line.strip()
    MT_PDBid[line] = 'NA'

# create all MT individual_list.txt for foldx
for id in MT_PDBid.keys():
    subprocess.call('touch individual_list_'+ id +".txt", shell=True)
#subprocess.call(print(MT_PDBid.keys())+'> MT_PDBuniq.txt',shell=True)

for line in totalMT_list:
    if re.match('#|\s',line) == None:
        #PDB_ID = re.findall(r'\w{4}',line)
        line=line.strip()
        PDB_ID = line.split('\t')[4]
        mt_info = line.split('\t')[5]+line.split('\t')[6]+line.split('\t')[7]+line.split('\t')[8]+";\n"
        f = open("individual_list_"+PDB_ID+".txt",'a')
        # xu: actually I don't think this action is good for a large data, open file mulitple times, is that time consuming?
        f.write(mt_info)

f.close()
totalMT_file.close()
subprocess.call('mv individual_list* ./pdb-files/' ,shell=True)
subprocess.call('mv MT_PDBonly.txt ./pdb-files/',shell=True)

