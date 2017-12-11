# input file: RNA.vcf file  ==> get ANN based on GRCh37.75 ==> get snpid based on dbsnp
# (here use filtered.vcf that QUAL>30 )
# dbsnp only use part of dbsnp
# output: filtered_ann.vcf and filtered_ann_snpid.vcf(with rsXXXX) and snpid.txt

java -Xmx4G -jar ../../snpEff_latest_core/snpEff/snpEff.jar -v GRCh37.75 ../result/filtered.vcf > ../result/filtered_ann.vcf

java -jar ../../snpEff_latest_core/snpEff/SnpSift.jar annotate -id dbsnp_1000000.vcf ../result/filtered_ann.vcf > ../reuslt/filtered_ann_snpid.vcf

#Xu: hard to change whole code, so here extract snpid separately
grep -v "#" ../result/filtered_ann_dbsnp.vcf | cut -f 1-3 | grep -v "\." > ../result/info_snpid.txt
