# INPUT : SIFT OUTPUT FILE

# OUTPUT : Only lines with Coding SNP's
# <Chr#> <Location> <ENSTid> <oldaa> <newaa> <posaa> <SIFT score> <SIFT med> <SIFT pred>


import sys


sift = sys.argv[1]

with open(sift,'r') as i:
    entries = i.readlines()

siftDict = {}
for lines in entries[1:]:
    data =(lines.rstrip('\n'))
    data = data.split('\t')
    data = lines.rstrip('\n')
    data = (data.split('\t'))
    region = data[8]
    chrome = data[0]
    location = data[1]
    refSNP = data[2]
    altSNP = data[3]
    ENSTid = data[4]
    oldAA = data[9]
    newAA = data[10]
    posAA = data[11]
    if len(altSNP) == 1:
        if region == 'NONSYNONYMOUS':
            key = chrome+':'+location
            SIFTscore = data[12]
            SIFTmed = data[13]
            SIFTpred = data[16]
            siftDict[key] = '\t' + ENSTid + '\t' + oldAA + '\t' + newAA + '\t' + posAA + '\t' + SIFTscore + '\t' + SIFTmed + '\t' + SIFTpred + '\t'



for snp in siftDict:
    print(snp + siftDict[snp])
