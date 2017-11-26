#### input a file contains PDB and uniprot file(first col is PDB id, second is uniprot id)
#### download all provided pdb in pdb-files folder and all protein fasta sequence in uniprotkb-files folder.

# run colton script: python parseID.py linesHuman_10 > PDBuniprot

mkdir pdb-files
mkdir uniprotkb-files
cut -f1 PDBuniprot | sort -u > ./pdb-files/PDBonly
cut -f2 PDBuniprot | sort -u > ./uniprotkb-files/UniprotKBonly

#following code never use since already download all in colton's script, here only for test and following foldx and pfam work.
#download provided pdb and uniprot.fasta
cd pdb-files
while read id
do
    wget "http://files.rcsb.org/download/$id.pdb"
done < PDBonly

cd ../uniprotkb-files
while read id
do
    wget "http://files.rcsb.org/download/$id.pdb"
done < UniprotKBonly


