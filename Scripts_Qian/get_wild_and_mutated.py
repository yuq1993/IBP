#!/usr/bin/python

# generate wild type and mutant type cds sequences and amino acid sequences

import re
from Bio.Seq import Seq
import Bio

# cds file
cds=open('../data/Homo_sapiens.GRCh37.75.cds.all.fa','r')
CDS={}
transcript=''
strand=''
seq=''
for line in cds:
    if line[0:1]=='>':
        if transcript != '':
            CDS[transcript]=[seq,strand]
            seq=''
        data=line.split()
        transcript=data[0].strip()[1:]
        strand=data[2].strip().split(":")[5]
        CDS[transcript]=[]
    else:
        seq+=line.strip()

CDS[transcript]=[seq,strand]
cds.close()
del line
del transcript
del strand
del seq

# first run sh new_01.sh 
# using filtered data
infile=open('new_info_fromSNPeff.target.txt','r')
for line in infile:
    data=line.split('\t')
    if data[0][0:5]=='chrom':
        continue
    chrom=data[0].strip()
    location=data[1].strip()
    ref=data[2].strip()
    alt=data[3].strip()
    transcript=data[9].strip()
    if transcript not in CDS:
        print(line.strip(),'\t',"ERROR: transcript not in cds file")
        continue
    else:
        seq=CDS[transcript][0]
        strand=CDS[transcript][1]
    s=data[10] # eg. c.898A->G
    nr=re.findall("\d+",s)
    nr=int(nr[0])
    t=s[0:1]
    if t!="c":
        print(line,'\t','Not_c')
    [r,a]=re.findall("[ATGC]",s)
    if strand == '1':
        if r!=ref or a!=alt:
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
    elif strand == '-1':
        if (ref=='A' and r!='T'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (ref=='T' and r!='A'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (ref=='G' and r!='C'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (ref=='C' and r!='G'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (alt=='A' and a!='T'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (alt=='T' and a!='A'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (alt=='G' and a!='C'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
        if (alt=='C' and a!='G'):
            print(line.strip(),'\t',"ERROR: ref, alt info not correct")
            continue
    if seq[nr-1] != r:
        print(line.strip(),'\t',"ERROR: ref location not correct",seq[nr-1])
        continue
    new_seq=seq[0:nr-1]+a+seq[nr:]
    old_seq=Seq(seq)
    sequence=Seq(new_seq)
    print(line.strip(),'\t',seq,'\t',old_seq.translate(),'\t',new_seq,'\t',sequence.translate())



