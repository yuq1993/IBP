#input file: info_fromSnpEff(only filtered_ann.vcf) ==> filter: only remain target SNP info ==> get ENST list
#output file: ENSTid.txt

#python ../Script_Qian/01.screenSNPs.py ../result/info_fromSNPeff.uniprot.transcripts_pdbs.txt > ../result/info_fromSnpEff_target.txt

#info_fromSNPeff.target.pdb_and_residue from Qian's result
cut -f 10 ../result/info_fromSNPeff.target.pdb_and_residue.txt | sort -u | sed '1d' > ENSTid.txt


