# input: Uniprotid from info_fromSNPeff.uniprot.transcripts_pdbs => all fasta sequences(ENST... or uniprot) => pFam
# output: all pfam info => uniprot_pfam.txt
# make sure pfam_scan.pl is executable
# need to specify PfamScan folder

mkdir uniprotkb-files
cd uniprotkb-files
#need to delete the header and blank row
#cut -f 14 ../../result/info_fromSNPeff.uniprot.transcripts_pdbs.txt | sed '1d' | sort -u | sed '1d' > uniprotID.txt
#TODO：extract ENST info
#cut -f 8


touch total_seq.fa
while read id 
do
	wget http://www.uniprot.org/uniprot/$id.fasta
	cat $id.fasta >> ../result/total_seq.fa
done < ../uniprotID.txt

#rm *.fasta

#AA sequence for pfam based on ENST
python ../Script_Colton/CDStoAA.py ../db/test_2000.gtf ../db/Homo_sapiens.GRCh37.75.dna.chromosome.1.fa > ../result/result_2000.fasta


#use test.fa first (unitprot)
#pfam_scan.pl --fasta ../result/total_seq.fa --dir ../PfamScan/ | grep -v '#' | sed '1d' > pfam_result.txt
#use AA.fasta from colton cdsTOaa.py (ENST)
#pfam_scan.pl --fasta ../result/total_seq.fa --dir ../PfamScan/ | grep -v '#' | sed '1d' > pfam_result.txt


