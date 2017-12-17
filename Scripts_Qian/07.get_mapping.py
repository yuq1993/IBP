#!/usr/bin/python

# Use mapping database: SIFTs

mapfile=open("../data/pdb_chain_uniprot.csv","r")
dict_2D={}
for line in mapfile:
    if(line[0]=='#' or line[0:3]=='PDB'):
        continue
    data=line.split(',')
    pdb,chain,uniprot,res_beg,res_end,pdb_beg,pdb_end,sp_beg,sp_end=data[0:]
    if uniprot in dict_2D:
        if pdb in dict_2D[uniprot]:
            dict_2D[uniprot][pdb].append([chain,res_beg,sp_beg])   # the beginning of uniprot on pdb and the beginning of pdb on uniprot
        else:
            dict_2D[uniprot][pdb]=[[chain,res_beg,sp_beg]]
    else:
        dict_2D[uniprot]={}
        dict_2D[uniprot][pdb]=[]
        new=[chain,res_beg,sp_beg]
        dict_2D[uniprot][pdb].append(new)

mapfile.close()

del pdb
del chain
del uniprot

infile=open("info_fromSNPeff.target.uniprot.transcripts_pdbs.checked.location.txt",'r')

for line in infile:
    data=line.split('\t')
    if (len(data) < 25):
        print(line.strip())
        continue
    else:
        uniprot=data[15].strip()
        location=int(data[25].strip())
        strand=data[24].strip()
        if uniprot in dict_2D:
            result=''
            for pdbs in dict_2D[uniprot]:
                for i in dict_2D[uniprot][pdbs]:
                    if strand == '-':
                        new_location=location-int(i[2])+int(i[1]) # strand '-'
                    else:
                        new_location=location+int(i[2])-int(i[1]) # new location = location  + uniprot_start -1 - pdb_start + 1 
                    result+=pdbs+'\t'+i[0]+'\t'+str(new_location)+'\t' # pdb chain new_location
            print(line.strip(),'\t','|||','\t',result)
        else:
            print(line.strip(),'\t','|||','\t','No Mapping info')
