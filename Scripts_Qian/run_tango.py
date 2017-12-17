#!/usr/bin/python

import os
import re

infile=open("../scripts/new_info_fromSNPeff.target.wild_and_mutated.txt",'r')
for line in infile:
    data=line.split('\t')
    if line.find("ERROR") != -1:
        print(line.strip())
        continue
    chrom=data[0].strip()
    pos=data[1].strip()
    ENST=data[9].strip()
    s=data[10] # eg. c.898A->G
    nr=re.findall("\d+",s)
    nr=int(nr[0])
    t=s[0:1]
    if t!="c":
        print(line.strip())
        continue
    p=data[11] # eg. p.Ile300Val
    pnr=re.findall("\d+",p)
    pnr=int(pnr[0])
    infname="./"+chrom+"/"+pos+ENST+"_mt.txt"
    if not os.path.exists(infname):
        print(line.strip(),'\t','ERROR:tango failed')
        continue
    inf=open(infname,'r')
    old_score=0
    for l in inf:
        if(l[0:3]=="res"): # Header
            continue
        d=l.split()
        old_score+=float(d[5].strip())
    inf.close()
    infname="./"+chrom+"/"+ENST+"_wt.txt"
    if not os.path.exists(infname):
        print(line.strip(),'\t','ERROR:tango failed')
        continue
    inf=open(infname,'r')
    new_score=0
    for l in inf:
        if(l[0:3]=="res"): # Header
            continue
        d=l.split()
        new_score+=float(d[5].strip())
    inf.close()
    print(line.strip(),'\t',old_score,'\t',new_score,'\t',new_score-old_score)
