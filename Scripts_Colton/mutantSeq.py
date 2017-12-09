#Input : $python mutantSeq.py <VCF file> <ENSTtoAA.py output>
### ENSTtoAA.py output ==  per/line ::: <ENST>;<chr#>;<strand>;<AAseq>;<ntSeq>;<CDSregions>

#Output for each VCF line
### <chr#> <location> <ENST> <WT AA Seq> <Mutant AA Seq> <AA substitution > <AA location>


import sys

##call in the VCF file
vcfFile = sys.argv[1] ## VCF File
enstFile = sys.argv[2] ## ENSTtoAA.py outputfile

with open(vcfFile,'r') as i:
    entries = i.readlines()

with open(enstFile,'r') as i:
    lines = i.readlines()

parsedVCF = []
for i in entries:
    if i[0] != '#':
        parsedVCF.append(i)

## Convert the ENSTtoAA.py to a Dictionary with the KEY == ENST ID
enstDict = {}
for i in lines:
    units = i.split(';')
    enstDict[units[0]] = units[1:]

snpDict = {}
for i in parsedVCF:
    info = i.split('\t')
    newkey = info[0] + ':' + info[1]
    snpDict[newkey] = info[5] ### DICT {<chr# : location > : <altSNP>}

### Goal : go through each KEY of the dictionary and find the SNP's with corresponding Chromosome and Location of the CDS regions

for snp in snpDict:
    print(snp)



