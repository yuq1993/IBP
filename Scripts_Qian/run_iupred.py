#!/usr/bin/python3




import os
import re
import subprocess

infile=open("new_info_fromSNPeff.target.wild_and_mutated.txt",'r')
i=0
for line in infile:
    i+=1
    data=line.split('\t')
    if line.find("ERROR") != -1:
        print(line.strip())
        continue
    s=data[10] # eg. c.898A->G
    nr=re.findall("\d+",s)
    nr=int(nr[0])
    t=s[0:1]
    if t!="c":
        print(line.strip())
        continue
    p=data[11] # eg. p.Ile300Val
    pnr=re.findall("\d+",p)
    pnr=pnr[0]
    file1=str(i)+"_old.seq"
    result=subprocess.run(['./iupred',file1,'long'],stdout=subprocess.PIPE)
    result=str(result.stdout)
    old_score=0
    for j in result.split('\\n'):
        if j.find('#') != -1 or j=="'":
            continue
        location=j.split()[0].strip()
        residue=j.split()[1].strip()
        score=j.split()[2].strip()
        if(location==pnr):
            old_score=score
    file2=str(i)+"_new.seq"
    result2=subprocess.run(['./iupred',file2,'long'],stdout=subprocess.PIPE)
    result2=str(result2.stdout)
    new_score=0
    for j in result2.split('\\n'):
        if j.find('#') != -1 or j=="'":
            continue
        location=j.split()[0].strip()
        residue=j.split()[1].strip()
        score=j.split()[2].strip()
        if(location==pnr):
            new_score=score
    print(line.strip(),'\t',pnr,'\t',old_score,'\t',new_score)
    cmd="rm "+str(i)+"_*.seq"
    os.system(cmd)
