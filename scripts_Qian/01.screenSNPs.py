#!usr/bin/python

# 过滤得到的vcf

import sys

inFile = sys.argv[1]

infile=open(inFile,'r')

for line in infile:
    data=line.split()
    Sequence_Ontology_term=data[6]
    if(Sequence_Ontology_term=="non_coding_transcript_variant" or Sequence_Ontology_term=="splice_region_variant&intron_variant" or Sequence_Ontology_term=="5_prime_UTR_variant" or Sequence_Ontology_term=="intergenic_region" or Sequence_Ontology_term=="synonymous_variant" or Sequence_Ontology_term=="non_coding_transcript_exon_variant" or Sequence_Ontology_term=="3_prime_UTR_variant" or Sequence_Ontology_term=="upstream_gene_variant" or Sequence_Ontology_term=="downstream_gene_variant" or Sequence_Ontology_term=="intron_variant" or Sequence_Ontology_term=="splice_donor_variant&intron_variant" or Sequence_Ontology_term=="splice_acceptor_variant&intron_variant" or Sequence_Ontology_term=="sequence_feature" or Sequence_Ontology_term=="5_prime_UTR_premature_start_codon_gain_variant" or Sequence_Ontology_term=="splice_region_variant" or Sequence_Ontology_term=="intergenic_region" or Sequence_Ontology_term=="structural_interaction_variant"):
        continue
    else:
        print(line.strip())
        
