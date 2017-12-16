#require file: ENSTid.txt, Homo_sapiens.GRCh37.75.cds.all.fa
#output: AA sequences with given transcript id

#########drop this method:
#require file: ENSTid.txt, ENST_AAseq.fa(from colton's script CDStoAA.py)
#python ../Script_Colton/CDStoAA.py ../db/test_2000.gtf ../db/Homo_sapiens.GRCh37.75.dna.chromosome.1.fa > ENST_AAseq_chr1_gtf2000.fasta
#NOTE: now only run chr1 and first 2000 gtf => ENST_AAseq_chr1_gtf2000.fa
#output: AA sequences with given transcript id

import re,Bio
from Bio.Seq import Seq

ENST_list = open('ENSTid.txt','r')
seq_file = open('../db/Homo_sapiens.GRCh37.75.cds.all.fa','r')
target_seq_file = open('target_ENST_seq.fa','w')
target_seqAA_file = open('target_ENST_AAseq.fa','w')

ENST_dic = {}
ENST_lines = ENST_list.readlines()

line = seq_file.readline()
ID=''
while line != '':
    if "ENST" in line:
        ID = re.findall("ENST\w+",line)[0]
        ENST_dic[ID] = line
    else:
        ENST_dic[ID] += line
    line = seq_file.readline()

for line in ENST_lines:
    ID = line.strip()
    if ID in ENST_dic.keys():
        newline = ENST_dic.get(ID)
        target_seq_file.write(newline)
target_seq_file.close()
target_seq_file = open('target_ENST_seq.fa','r')

line = target_seq_file.readline()
ID =''
ENST_dic = {}
while line != '':
    if "ENST" in line:
        ID = re.findall("ENST\w+",line)[0]
        ENST_dic[ID] = line
    else:
        line = line.strip()
        seq = Seq(line)
        ENST_dic[ID] += str(seq.translate()) + '\n'
    line = target_seq_file.readline()

for line in ENST_lines:
    ID = line.strip()
    if ID in ENST_dic.keys():
        newline = ENST_dic.get(ID)
        target_seqAA_file.write(newline)

target_seqAA_file.close()
target_seq_file.close()
ENST_list.close()
seq_file.close()
