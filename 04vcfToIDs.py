#Input: a VCF file
#Output: information for each SNP seperated by tab as follows, suitable for the G column in coordinate table
# chr# | location | refSNP | altSNP | QUAL | DP | ENSG | ENST


import sys
import re


inFile = sys.argv[1]

with open(inFile,'r') as i:
    entries = i.readlines()


parsedFile = []


### Removes the header information leaving only lines with data for each SNP
for i in entries:
    if i[0] != '#':
        parsedFile.append(i)

### prints header for output

print('chrom' + '\t' + 'location' + "\t" + 'refSNP' + '\t' + 'altSNP' + '\t' +' QUAL' + '\t' + 'DP' + '\t' + 'Sequence_Ontology_term' + '\t' + 'Impact' + '\t' + 'ENSG' + '\t' + 'ENST')

### collects the data
for i in parsedFile:
    longData = []
    geneData = []
    info = i.split('\t')
    chrom = info[0]
    location = info[1]
    refSNP = info[3]
    altSNP = info[4]
    QUAL = info[5]
    geneData = info[7]
    infoData = geneData.split(';')
    DP = infoData[0]
    for i in infoData:
        if i[0:3] == 'ANN':
            y = i
    longData = y.split('|')
    geneANDtrans = []
    count = 0
    for i in longData:
        if i[0:4] == 'ENSG':
            if '-' in i and longData[count-1] == 'intergenic_region' :
                count +=1
                continue
            else:
                geneANDtrans.append(longData[count-3] + '\t' + longData[count-2] + '\t' + longData[count] + '\t' + longData[count+2])
        count +=1
        
    for i in geneANDtrans:
        print( chrom + '\t' + location + '\t' + refSNP + '\t' + altSNP + '\t' + QUAL + '\t' + DP + '\t' + i)

