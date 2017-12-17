#!/usr/bin/python

import os
import re

infile=open("new_info_fromSNPeff.target.wild_and_mutated.txt",'r')
i=0
for line in infile:
    i+=1
    data=line.split('\t')
    if line.find("ERROR") != -1:
        continue
    old_seq=data[12].strip()
    old_AA=data[13].strip()
    new_seq=data[14].strip()
    new_AA=data[15].strip()
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
    outf_name=str(i)+"_old.seq"
    outf=open(outf_name,"w")
    outf.write(">"+str(i))
    outf.write("\n")
    outf.write(old_AA)
    outf.close()
    outf2_name=str(i)+"_new.seq"
    outf2=open(outf2_name,'w')
    outf2.write(">"+str(i))
    outf2.write("\n")
    outf2.write(new_AA)
    outf2.close
