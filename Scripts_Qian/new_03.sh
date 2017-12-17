#uniq  mapping_info_transcriptslist.txt > mapping_info_transcriptslist_uniq.txt
#sort mapping_info_transcriptslist_uniq.txt|uniq > mapping_info_transcriptslist_uniq2.txt
#rm mapping_info_transcriptslist_uniq.txt
#mv mapping_info_transcriptslist_uniq2.txt mapping_info_transcriptslist_uniq.txt
cut -f 10 new_info_fromSNPeff.target.txt > new_info_fromSNPeff.target_transcriptlist.txt
sed '1d' new_info_fromSNPeff.target_transcriptlist.txt > tmp
rm new_info_fromSNPeff.target_transcriptlist.txt
mv tmp new_info_fromSNPeff.target_transcriptlist.txt
python get_pdb_and_residue.py > new_info_fromSNPeff.target.pdb_and_residue.txt 

