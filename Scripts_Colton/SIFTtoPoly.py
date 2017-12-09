#INPUT: THE XLS file from the SIFT results
### $python thisScript.py <Sift.XLS>

#OUTPUT: The batch file for the Polyphen input



import sys



SIFToutput = sys.argv[1]

with open(SIFToutput,'r') as i:
    entries = i.readlines()


for lines in entries[1:]:
    data = (lines.split('\t'))
    chrome = data[0]
    location = data[1]
    refSNP = data[2]
    altSNP = data[3]
    region = data[8]
   # SIFTscore = data[12]
   # SIFTmed = data[13]
    if len(altSNP) == 1:
        if region == 'NONSYNONYMOUS':
            print(chrome+':'+location+'\t'+refSNP+'/'+altSNP)

