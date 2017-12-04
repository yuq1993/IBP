#!/usr/bin/python

# We are going to check whether transcripts snp modified can have impact on uniprot

infile=open('info_fromSNPeff.target.uniprot.transcripts_pdbs.txt','r')

for line in infile:
    data=line.split('\t')
    transcriptID=data[9].strip()
    if(len(data)>21):
        transcript=data[21]
    else:
        print(line.strip())
        continue
    transcripts=transcript.split(';')
    for i in range(len(transcripts)):
        transcripts[i]=transcripts[i].replace(' ','')
    if(transcriptID in transcripts):
        print(line.strip())
        continue
    else:
        print(line.split("|||")[0].strip(),'\t','|||','\t',line.split("|||")[1].strip())
