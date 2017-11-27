

import sys

inFile = sys.argv[1]

with open(inFile,'r') as i:
    entries =  i.readlines()


parsedEntries = []

for i in entries:
    if i[0] != '#':
        parsedEntries.append(i)




for i in parsedEntries:
    line  = i.split(';')
    ENST = (line[1]).split(' ')
    ENST = ENST[2]
    info = line[0].split('\t')
    if info[2] == 'CDS':
        print(info[2] + '\t' + ENST)
