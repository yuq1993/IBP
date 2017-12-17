#!/usr/bin/python

# This script adds transcript location into data

infile=open('../data/transcripts_start_location.txt','r')

transcriptID={}

for line in infile:
    data=line.split()
    transcriptID[data[0]]=[data[2],data[3]]

infile2=open('info_fromSNPeff.target.uniprot.transcripts_pdbs.checked.txt','r')
for line in infile2:
    data=line.split('\t')
    if(len(data)>21):
        transcript=data[9].strip()
    else:
        print(line.strip())
        continue
    if(transcript in transcriptID):
        print(line.strip(),'\t','|||','\t','\t'.join(transcriptID[transcript]))
    else:
        print(line.strip(),'\t','|||','\t',"ERROR:not in dict:",transcript)



    
