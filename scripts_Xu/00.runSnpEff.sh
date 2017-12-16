# input file: RNA.vcf file  ==> get ANN based on GRCh37.75 ==> get snpid based on dbsnp
# (here use filtered.vcf that QUAL>30)
# dbsnp only use part of dbsnp
# output: filtered_ann.vcf and filtered_ann_snpid.vcf(with rsXXXX) and snpid.txt

java -Xmx4G -jar ../../snpEff_latest_core/snpEff/snpEff.jar -v GRCh37.75 ../result/RNAseq_MM001.nofirst1bp.dedup.vcf > ../result/RNAseq_MM001_ANN.vcf

java -jar ../../snpEff_latest_core/snpEff/SnpSift.jar annotate -id ../../snpEff_latest_core/snpEff/db/dbSNP/00-common_all.vcf ../result/RNAseq_MM001_ANN.vcf > ../result/info_fromSNPeff_snpid.vcf

