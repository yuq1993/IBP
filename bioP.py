# Input : Human Genome Annotation File

# Output : ENST Id's and the locations of their associated CDS regions in the genome
    # ENST ID | Chr | START | END | STRAND| FRAME

# FRAME INFO : 0 , 1 ,2 means the first base of the feature is the fist base of codon, second base of codon , third base of codon

# Purpose : We want to use these CDS regions to locate the COLLECTIVE genomic regions

# How to : from bash line $python THIS_SCRIPT.py <Human annotation File>


import sys
from Bio.Seq import Seq
import Bio

inFile = sys.argv[1] ### Human Annotation File
chrFasta = sys.argv[2]



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
    line  = i.split(';')
    ENST = (line[1]).split(' ')
    ENST = ENST[2][1:-1]
    info = line[0].split('\t')
    if info[2] == 'CDS':
        if ENST not in ENSTlocations.keys():
            ENSTlocations[ENST] = ''
            ENSTlocations[ENST] += str(info[6]) + ' ' + str(info[0]) + ' | '
#        print(ENST + '\t' +  'chr ' + info[0]  + '\t' + info[3] + '\t' + info[4] + '\t' + info[6] + '\t' + info[7])
        ENSTlocations[ENST] += str(info[3]) + '_' +  str(info[4]) + ' '



for key in ENSTlocations:
    split1 = ENSTlocations[key].split('|') # splits VALUE into the strand, chromsome AND locations
    split2 = split1[0].split(' ') # splits the strand and chromosome
    split3 = split1[1].split(' ') # splits the individual locations seperated by a _
    ## getting the sequence
    sequence = ''
    splitKey =key, ENSTlocations[key].split(' ')
    strand = splitKey[1][0]
    chromNumber = splitKey[1][1]
 #   print(key,ENSTlocations[key])
    nucleotideSequnce = ''

    for i in split3[1:-1]: ### this covers all the different regions a transcript may be split into
        startend = i
        startend = startend.split('_')
        start = int(startend[0])
        end = int(startend[1])
        sequence += str(data[int(start)-1:int(end)])
        """
        if split2[0] == '-': ## only if it is on - strand
            sequence = sequence[::-1]
            newseq= ''
            for x in sequence:
                if x == 'A' or 'a':
                    newseq += 'T'
                elif x == 'T' or 't':
                    newseq += 'A'
                elif x == 'G' or 'g':
                    newseq += 'C'
                else:
                    newseq += 'G'
            sequence = newseq
        """
     #   mysequence = Seq(sequence)
    #    if split2[0] == '-':
   #        mysequence = mysequence.complement()
  #         transcribe =transcribe(sequence)
 #       else:
#           transcribe = transcribe(sequence)
    print(key + ' : ' +  sequence)

