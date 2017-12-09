# Input : CDS lines of the Human Genome Annotation File and the chromosome fasta

# $python ENSTtoAA.py <GTF>  <chromosome fasta>

# Output : Outputs a LIST where each line is [ENST, chromsome #, Strand, AA Sequence, NT Sequence, CDS Regions] 


import sys
from Bio.Seq import Seq
import Bio

inFile = sys.argv[1] ### Human Annotation File
chrFasta = sys.argv[2] ### Chromosome Fasta


with open(inFile,'r') as i:
    entries =  i.readlines()

with open(chrFasta,'r') as i:
    data = i.readlines()

chr1string = ''

for i in data[1:]:
    chr1string += i.strip('\n')

data=chr1string

parsedEntries = []

for i in entries: # Remove header in an un-efficient manner
    if i[0] != '#':
        parsedEntries.append(i)

ENSTlocations = {}
for i in parsedEntries:
    columns = i.split('\t')
    if columns[1] == 'protein_coding' or "protein coding":
        if columns[2] == 'CDS':
            line  = i.split(';')
            ENST = (line[1]).split(' ')
            ENST = ENST[2][1:-1]
            info = line[0].split('\t')
   #         print(info)
            if ENST not in ENSTlocations.keys():
                ENSTlocations[ENST] = ' ' + info[0] + ' ' + info[6] + ' '
            ENSTlocations[ENST] += info[3] + '_' + info[4] + ';'

'''
for key in ENSTlocations:
    print(key + ENSTlocations[key])
'''

ENSTdict = {}
totalSequences = []
for key in ENSTlocations:
    splitValue = ENSTlocations[key].split(' ') # split into list [ <chr#> <strand> <CDSlocations;CDSlocations>
    chromosome = splitValue[1] # splits the strand and chromosome
    strand = splitValue[2]
    listRegions = splitValue[3].split(';') # splits the individual locations seperated by a _
    listRegions = listRegions[:len(listRegions)-1]
## Retrieveing the sequence
    sequence = ''

    for i in listRegions: ### this covers all the different regions a transcript may be split into
        startend = i.split('_')
        start = int(startend[0])
        end = int(startend[1])
        if strand == '-':
            sequence = str(data[int(start)-1:int(end)]) + sequence
        else:
            sequence += str(data[int(start)-1:int(end)])

    if strand == '-': ## only if it is on - strand
        sequence = sequence[::-1]
        newseq= ''
        for x in sequence:
            if x == 'A' or x ==  'a':
                newseq += 'T'
            elif x == 'T' or x == 't':
                newseq += 'A'
            elif x == 'G' or x == 'g':
                newseq += 'C'
            else:
                newseq += 'G'
        sequence = newseq
    sequence = Seq(sequence)
   # totalSeq.append(sequence)
    ENSTdict[ENST] = sequence
   # print(key + ' ' + strand +  ' : ' + sequence , listRegions)
    if '*' not in sequence.translate():
        print(key + ';' + chromosome +  ';'  + strand +  ';' + sequence.translate() + ';' + sequence +  ';' + str(listRegions))
       # ENSTdict[ENST] = chromosome +  ';'  + strand +  ';' + sequence.translate() + ';' + sequence + ';' + str(listRegions) 

