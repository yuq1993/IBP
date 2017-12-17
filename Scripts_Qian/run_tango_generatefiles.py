#!/usr/bin/python


#tango2_3_1 P05100 ct="N" nt="N" ph="7.4" te="303" io="0.05" seq="DNEWGYIAYHVSQDP"

import os
import re

infile=open("new_info_fromSNPeff.target.wild_and_mutated.txt",'r')
transcriptlist={}
for line in infile:
    data=line.split('\t')
    pos=data[1].strip()
    transcript=data[9].strip()
    if line.find("ERROR") != -1:
        continue
    old_seq=data[12].strip()
    old_AA=data[13].strip()
    if old_AA[-1]=="*":
        old_AA=old_AA[0:-1]
    new_seq=data[14].strip()
    new_AA=data[15].strip()
    if new_AA[-1]=="*":
        new_AA=new_AA[0:-1]
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
    outfname=transcript+"_wt.sh"
    outf=open(outfname,'w')
    # for wt if transcriptID same, then sequence same
    if transcript not in transcriptlist:
        cmd="tango2_3_1 "+transcript+"_wt "+"ct=\"N\" nt=\"N\" ph=\"7.4\" te=\"303\" io=\"0.05\" seq=\""+old_AA+"\" >/dev/null 2>&1"
        outf.write(cmd)
        outf.close()
        print(transcript+"_wt.sh")
    outfname=pos+transcript+"_mt.sh"
    outf=open(outfname,'w')
    cmd2="tango2_3_1 "+pos+transcript+"_mt "+"ct=\"N\" nt=\"N\" ph=\"7.4\" te=\"303\" io=\"0.05\" seq=\""+new_AA+"\" >/dev/null 2>&1"
    outf.write(cmd2)
    outf.close()
    print(pos+transcript+"_mt.sh")

