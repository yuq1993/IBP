# INPUT : $python thisScript.py <SIFT_output> <Polyphen Output>

# OUTPUT : <chr#>:<location> <SIFT score> <SIFT median> <SIFT prediction> <pph2 prob> <pph FPR> <pph TPR> <Polyphen Prediction>

# also get from SIFT the aa old , aa new , aa POS

import sys

siftOut = sys.argv[1]
polyOut = sys.argv[2]

with open(siftOut,'r') as i:
    siftEntries = i.readlines().rstrip('\n')

with open(polyOut,'r') as i:
    polyEntries = i.readlines().rstrip('\n')
    

parsePoly = []
for i in polyEntries:
    if i[0] != '#':
        parsePoly.append(i)

polyDict = {}
for i in parsePoly:
    data = i.split('\t')
    chrloc = data[13].split('|')
    key = chrloc[0][2:] # chr#:location
    polyPred = data[9]
    pph2prob = data[10]
    pph2FPR = data[11]
    pph2TPR =  data[12]
    polyDict[key] = '\t' + pph2prob + '\t' + pph2FPR + '\t' + pph2TPR + '\t' + polyPred +'\t'



siftDict = {}
for lines in siftEntries[1:]:
    data = (lines.split('\t'))
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
            if key in polyDict.keys():
                SIFTscore = data[12]
                SIFTmed = data[13]
                SIFTpred = data[16]
                siftDict[key] = '\t' + ENSTid + '\t' + oldAA + '\t' + newAA + '\t' + posAA + '\t' + SIFTscore + '\t' + SIFTmed + '\t' + SIFTpred + '\t'


# now link the dictionary entries

for snp in siftDict:
    hit = snp + siftDict[snp] + polyDict[snp]
    print(hit)



"""
    DATA
        ('   370', 1)
        ('    V', 2)
        ('    M', 3)
        ('rs150122  ', 4)
        ('Q8IYT8    ', 5)
        ('   370', 6)
        ('  V', 7)
        ('  M', 8)
        ('            benign', 9)
        ('         0', 10)
        ('         1', 11)
        ('         1', 12)
        ('# chr17:19713740|CT|uc002gwn.2-|ULK2|NP_055498\n', 13)
"""
