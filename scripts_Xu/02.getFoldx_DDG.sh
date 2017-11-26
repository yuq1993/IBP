#### required: individual_list_XXXX.txt(mutation info file) for each mutation, WT.pdb, rotabase.txt(foldx need)
#### make sure foldx is executable

cd pdb-files

while read id
do
    foldx --command=BuildModel --pdb=$id.pdb --mutant-file=individual_list_$id.txt
done < PDBonly

# put all the DDG result in DDG_fxout
# TODO: add the mutation info(position,ref_AA,alt_AA)
for f in Dif_*.fxout
do
    grep "pdb" f >> DDG_fxout
done

