#get info from snpeff and put in the coordinate table (e.g. ENST,ENSG,SNPid)
#input:

#file for coordinate table
cut -f 1-6,9,10,13,16 ../result/info_fromSNPeff.target.uniprot.txt | sed '1d' > ../result/info_ENSG_ENST_uniprot.txt

#Xu: hard to change whole code, so here extract snpid separately
grep -v "#" ../result/info_fromSNPeff_snpid.vcf | cut -f 1-3 | grep -v "\." > ../result/info_snpid.txt


