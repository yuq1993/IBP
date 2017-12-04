#!usr/bin/python

infile=open("../Scripts_Colton/gtf2AA.txt",'r')
transcript=''
chrom=0
chromID=0
start=0
end=0
strand=''
frame=0
for line in infile:
    data=line.split()
    if(data[3]=='|' or len(data)==4):
        if(strand=='+' and transcript != ''):
            print(transcript,'\t',chromID,'\t',strand,'\t',start)
        elif(strand=='-' and transcript != ''):
            print(transcript,'\t',chromID,'\t',strand,'\t',end)
        transcript=''
        continue
    if(data[0]!=transcript):
        if(strand=='+' and transcript != ''):
            print(transcript,'\t',chromID,'\t',strand,'\t',start)
        elif(strand=='-' and transcript != ''):
            print(transcript,'\t',chromID,'\t',strand,'\t',end)
        transcript,chrom,chromID,start,end,strand,frame=data[0:]
    elif(data[0]==transcript and strand=='+'):
        if(data[3]<start):
            start=data[3] # find smallest start position for positive strand transcripts
    elif(data[0]==transcript and strand=="-"):
        if(data[4]>end):
            end=data[4] # find biggest location on genome as start position for negative strand transcripts
    else:
        print("Error")
    
infile.close()

