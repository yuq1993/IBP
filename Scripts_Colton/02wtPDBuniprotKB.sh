
### Purpose : Get Wild-Type protein PDB's from UniprotKB Database

#pulls the PDB accession numbers from human proteins in the uniprotKB DB



curl http://www.uniprot.org/docs/pdbtosp > pdblist
cat pdblist | grep HUMAN > linesHuman
cat pdblist | grep HUMAN | grep -o '>....<' | cut -c2-5 > humanPDBids
python parseID.py linesHuman > PDBuniprot

cut -f1 PDBuniprot > PDBonly
cut -f2 PDBuniprot > UniprotKBonly

rm lineHumans
rm pdblist

#curl http://www.uniprot.org/docs/pdbtosp > pdbtosp
#cat pdbtosp | grep HUMAN | grep -o '>....<' | cut -c2-5 > humanPDBids

#!/bin/bash
mkdir uniprotkb-pdb-files
mv humanPDBids ./uniprotkb-pdb-files
cd uniprotkb-pdb-files
input="humanPDBids"
while read -r var
do
  wget "http://www.rcsb.org/pdb/files/$var.pdb"
done < "$input"

