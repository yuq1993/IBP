
sh new_01.sh # screen snp, generate target file
sh new_02.sh # python get_wild_and_mutated.py > new_info_fromSNPeff.target.wild_and_mutated.txt, generate wild type AA sequence and mutant AA sequence
sh new_03.sh # python get_pdb_and_residue.py > new_info_fromSNPeff.target.pdb_and_residue.txt, generate pdb and residue from mapping file.
# SNPs which satify all criteria (have mapping info, without confix annotation) are marked 'PASS', so next step can grep 'PASS' to get all mutations.



