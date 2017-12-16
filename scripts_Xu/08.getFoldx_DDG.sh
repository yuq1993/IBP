#### required: individual_list_XXXX.txt(mutation info file) for each mutation, WT.pdb, rotabase.txt(foldx need)
#### MT_PDBonly.txt
#### make sure foldx is executable

cd pdb-files

while read id
do
    foldx --command=BuildModel --pdb=$id.pdb --mutant-file=individual_list_$id.txt
done < MT_PDBonly.txt

# put all the DDG result in DDG_fxout
for f in Dif_*.fxout
do
    grep "pdb" $f >> DDG_fxout.tmp
done

sort -u DDG_fxout.tmp > DDG_fxout.txt
rm DDG_fxout.tmp
