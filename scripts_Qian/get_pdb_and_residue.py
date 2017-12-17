#!/usr/bin/python

# run sh new_03.sh

import re
from Bio.Seq import Seq
import Bio

# loading uniq transcript list
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

aa_dict_3to1 = {'ALA':'A','CYS':'C','ASP':'D','GLU':'E','PHE':'F','GLY':'G','HIS':'H','H1S':'H','H2S':'H','ILE':'I','LYS':'K','LEU':'L','MET':'M','ASN':'N','PRO':'P','GLN':'Q','ARG':'R','SER':'S','THR':'T','VAL':'V','TRP':'W','TYR':'Y'}

# mapping text

infile=open('../data/PSX_map_PDB_to_CDS.txt','r')
for line in infile:
    data=line.split('\t')
    pdb=data[0].strip()
    chain=data[1].strip()
    residue_3=data[2].strip()
    if residue_3 not in aa_dict_3to1:
        residue="GAP"
    elif residue_3 != "GAP":
        residue=aa_dict_3to1[residue_3]
    else:
        residue=residue_3
    residue_nr=int(data[3].strip())
    transcript=data[4].strip().split()[0]
    coordinate=int(data[5].strip())+1 # change from 0-index into 1-index
    codon=data[6].strip()
    #print(transcript)
    if transcript not in target_transcript:
        continue
    if transcript in mapping:
        mapping[transcript].append([pdb,chain,residue_nr,coordinate,codon,residue])
    else:
        mapping[transcript]=[]
        mapping[transcript].append([pdb,chain,int(residue_nr),int(coordinate),codon,residue])
infile.close()
# test code
#print(mapping["ENST00000520777"])
#al=mapping["ENST00000520777"]
#del line
#for idx in range(0,len(al)):
#    print(idx)

#exit()

# get from sh new_01.sh
# filtered data
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
    if transcript not in transcriptlist:
        print(line.strip(),'\t',"transcript_not_in_mapping")
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
                    # this snp between al[idx][3] and al[idx+1][3]
                    ref2=al[idx][4][nr-al[idx][3]] # eg. if nr=786, al[idx][3]=784, then snp is at the last position on codon. 
                    if ref2!=r:
                        print(line.strip(),'\t',al[idx],'\t','ERROR:ref_info_not_correct') # ref2 should be equal to r (ref info given by SNPeff)
                        break
                    new_codon=al[idx][4][0:nr-al[idx][3]]+a+al[idx][4][nr-al[idx][3]+1:]
                    new_AA=Seq(new_codon).translate()
                    if al[idx][5] == "GAP":
                        print(line.strip(),'\t',al[idx],'\t',new_AA,'SNP_in_PDB_GAP')
                        break
                    else:
                        print(line.strip(),'\t',al[idx],'\t',new_codon,'\t',new_AA,'PASS') # use "PASS" as identifier in order to screen SNPs
                        break
                elif al[idx+1][3]-al[idx][3]<3:
                    print(line.strip(),'\t',"ERROR:two_coordinate_distance_shorter_than_3") # because of two coordinate distance shorter than 3
                    break
                elif al[idx+1][3]-al[idx][3]>3 and nr-al[idx][3]>=3:
                    print(line.strip(),'\t',"SNP_in_transcript_gap")
                    break
                elif al[idx+1][3]-al[idx][3]>3 and nr-al[idx][3]<3:
                    print(line.strip(),'\t',nr,'\t',al[idx][3],'\t',al[idx+1],"There_is_gap_here_but_SNP_not_in_gap")
                    break
                elif al[idx][3] > nr:
                    print(line.strip(),'\t',"Beginning_gap")
                    break
        if(flag==0):
            print(line.strip(),'\t','Ending_gap')

    else:
        print(line.strip(),'\t',"transcript_not_in_mapping")

