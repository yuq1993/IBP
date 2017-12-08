#!/usr/bin/python

import re
mapping={}
transcriptlist={}
infile=open('mapping_info_transcriptslist_uniq.txt','r')
for line in infile:
    transcript=line.strip()
    transcriptlist[transcript]=1

infile.close()
del transcript

target_transcript={}
infile=open('new_info_fromSNPeff.target_transcriptlist.txt','r')
for line in infile:
    transcript=line.strip()
    target_transcript[transcript]=1

infile.close()
del transcript


infile=open('../data/PSX_map_PDB_to_CDS.txt','r')
for line in infile:
    data=line.split('\t')
    pdb=data[0].strip()
    chain=data[1].strip()
    residue=data[7].strip()
    residue_nr=int(data[3].strip())
    transcript=data[4].strip().split()[0]
    coordinate=int(data[5].strip())
    codon=data[6].strip()
    #print(transcript)
    if transcript not in target_transcript:
        continue
    if transcript in mapping:
        mapping[transcript].append([pdb,chain,residue_nr,coordinate,codon])
    else:
        mapping[transcript]=[]
        mapping[transcript].append([pdb,chain,int(residue_nr),int(coordinate),codon])
infile.close()
# test code
#print(mapping["ENST00000520777"])
#al=mapping["ENST00000520777"]
#del line
#for idx in range(0,len(al)):
#    print(idx)

#exit()


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
    print(transcript)
    if transcript not in transcriptlist:
        print(line,'\t',"transcript_not_in_mapping")
        continue
    s=data[10] # eg. c.898A->G
    nr=re.findall("\d+",s)
    nr=int(nr[0])
    t=s[0:1]
    if t!="c":
        print(line,'\t','Not_c')
    [r,a]=re.findall("[ATGC]",s)
    if transcript in mapping:
        al=mapping[transcript] # all mapping info in this transcript
        #print(al)
        flag=0
        for idx in range(0,len(al)):
            if al[idx][3] <= nr-3:
                continue
            else:
                flag=1
                if al[idx+1][3] > nr and al[idx+1][3]-al[idx][3]==3 and al[idx][3] < nr:
                    print(line,'\t',nr,'\t',al[idx][3],'\t',al[idx+1])
                elif al[idx+1][3]-al[idx][3]<3:
                    print(line,'\t',"ERROR:two_coordinate_distance_shorter_than_3") # because of two coordinate distance shorter than 3
                elif al[idx+1][3]-al[idx][3]>3 and nr-al[idx][3]>=3:
                    print(line,'\t',"SNP_in_gap")
                elif al[idx+1][3]-al[idx][3]>3 and nr-al[idx][3]<3:
                    print(line,'\t',nr,'\t',al[idx][3],'\t',al[idx+1],"There_is_gap_here_but_SNP_not_in_gap")
                elif al[idx][3] > nr:
                    print(line,'\t',"Beginning gap")
                    break
        if(flag==0):
            print(line,'\t','Ending gap')
        
    else:
        print(line,'\t',"transcript_not_in_mapping")


