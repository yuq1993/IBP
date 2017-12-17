# not used in SNPeffect project

#convert2annovar.pl -format vcf4 ../data/RNAseq_MM001.nofirst1bp.dedup.vcf  > ../data/RNAseq_MM001.nofirst1bp.dedup.vcf.avinput
#table_annovar.pl ../data/RNAseq_MM001.nofirst1bp.dedup.vcf.avinput /Users/yuqian/linux_software/annovar/humandb/ -buildver hg19 -out ../output/RNAseq_MM001 -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation gx,r,f,f,f -nastring . -csvout -polish
annotate_variation.pl -geneanno -dbtype refGene -buildver hg19 ../data/RNAseq_MM001.nofirst1bp.dedup.vcf /Users/yuqian/linux_software/annovar/humandb/ --outfile ../output/RNAseq_MM001
