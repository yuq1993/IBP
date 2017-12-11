#input file: info_fromSnpEff(only filtered_ann.vcf) ==> filter: only remain target SNP info ==> get ENST list
#output file: ENSTid.txt

python ../Script_Qian/01.screenSNPs.py ../result/info_fromSNPeff.uniprot.transcripts_pdbs.txt > ../result/info_fromSnpEff_target.txt

cut -f 10 ../result/info_fromSnpEff_target.txt | sort -u | sed '1d' > ENSTid.txt

#file for coordinate table
grep -v NA ../result/info_fromSnpEff_target.txt | cut -f 1-8,14 | sed '1d' > ../result/info_ENSG_ENST_uniprot.txt

