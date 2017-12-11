#input file: target_ENST_AAseq.fa (after run 00.getAAfromENST.py) => run pfam software get domain info
#output file: ENST_pfam.txt
#make sure pfam_scan.pl is executable
#need to specify PfamScan folder

#pfam_scan.pl --fasta ../Script/Script_Xu/target_ENST_AAseq.fa --dir ../PfamScan/ > ../Script/Script_Xu/pfam_ENST_result_tmp.txt

grep -v "#" pfam_ENST_result_tmp.txt | sed '1d' > pfam_ENST_result.txt
rm pfam_ENST_result_tmp.txt
