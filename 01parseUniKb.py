# Author : Colton Gowan
# 
# Input : html of pdb-uniprotkb of lines containing HUMAN from grep command
# Output : file with column 1 = unprotKB accession # | column2 = pdb ID

import sys
import re
"""
inFile = sys.argv[1]

with open(inFile,'r') as i:
    entries = i.readlines()

"""
#First we must prepare the HTML file by parsing it into a workable format
#Some PDB-ID's have multiple organisms associated with them.



while i <= len(entries):
    if entries[i] == '<':
        i = lastgood
        i+=1
    while entries[i][0] != '<':
        entries[lastgood] = entries[lastgood] + entries[i]
        i+=1

"""
for i in range(0,len(entries)): # this loop appends the multilines together
    if entries[i][0] != '<':
        entries[i-1] = entries[i-1] + entries[i]

wildtypeList = []
wildtypeIDS = {}
testlist = []
count = 0
for line in entries:
    #if loop extracts the PDB-ID which may belong to multiple Human UniprotKB-ID's
    if line[0] == '<':
        pdbID = line[0:64]
        pdbID = re.search('(?<=>)\w*(?=<)',pdbID)
        pdbID = pdbID.group(0)
        uniprotkbID = line[65:]
        count += 1
        
        if "," in uniprotkbID: # if there is a comma, there are multiple organisms w/ same PDB-ID. These must then be checked if there are multiple human hits which have unique UniprotKB-ID's
            hits = uniprotkbID.split(",")
            for organisms in hits:
                if "HUMAN" in organisms:
                    humanhit = re.search('(?<=>)\w*(?=<)',organisms)
                    humanhit = humanhit.group(0)
                    wildtypeList.append(pdbID+"\t"+ humanhit)
                   # wildtypeIDS[humanhit] = pdbID
        else: #this loop is for single human PDB-ID's
            human = re.search('(?<=>)\w*(?=<)',uniprotkbID)
            human = human.group(0)
            wildtypeList.append(pdbID+"\t"+human)
           # wildtypeIDS[human] = pdbID

for id in wildtypeList:
    print id
"""
