#!/usr/bin/python

# sum up tango score as domains
import os
domains=[]
infile=open('../../data/pfam_ENST_table.txt','r')
#ENST00000001008 43      135     FKBP_C  Domain
transcript=''
for line in infile:
    data=line.split()
    ENST=data[0].strip()
    start=data[1].strip()
    end=data[2].strip()
    name=data[3].strip()
    d_type=data[4].strip()
    if ENST != transcript:
        if transcript != '':
            scores={}
            if os.path.exists(transcript+'_wt.txt'):
                result_wt=open(transcript+'_wt.txt','r')
                # 01        M       0.1     0.0   0.000   0.000   0.000
                for l in result_wt:
                    if l[0:3]=='res':
                        continue
                    d=l.split()
                    nr=int(d[0].strip())
                    residue=d[1].strip()
                    score=float(d[5].strip())
                    scores[nr]=score
                result_wt.close()
                for i in domains:
                    s=0
                    for j in scores.keys():
                        if i[0] <= j <= i[1]:
                            s+=scores[j]
                    print(i[2],"\t",s)
        domains=[]
        transcript=''
        domains.append([int(start),int(end),line.strip()])
        transcript=ENST
    else:
        domains.append([int(start),int(end),line.strip()])
    


