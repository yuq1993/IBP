# running scripts order and its function

part1: annotation from SnpEff
1.sh 00.runSnpEff.sh ==> get ENST,ENSG,rsXXX etc info
2.sh01.getCoordinate.sh ==> get info to write in mysql database coordinate table (info_ENST_ENSG.txt  && info_snpid.txt)

part2: run Pfam
1.sh 02.getENSTidList.sh  ==> get ENSTid.txt(target ENST) 
2.python 03.getAAfromENST.py ==>  get target_ENST_AAseq.fa for pfam software3.go to pfam folder + sh 04.getPfam_fromENST.sh => pfam_ENST_reuslt 
4.python 05.getPfam_fromENST.py => get info to write in WT table (pfam_ENST_table.txt)

part3: FoldX
1.python 06.createPDB_list.py => individual_list.txt(including all mutation info that needs to generate individual_list.txt for each mutation) & snp_PDB_info.txt(info about filtered mutations that have PDB id)
2.python 07.createMTinduvidual_list.py => generate all indivual_list_PDBID.txt for each mutations
3.sh 08.getFoldx_DDG.sh ==> get DDG results(DDG_fxout.txt)
4.python 09.getFoldx_DDG.py ==> get DDG results to write in MT table(result_DDG.txt)

part4:IUPred Tango SIFT PolyPhen
1.sh 10.get_iupred_tango.sh ==> get IUPred/Tango wt and mt score to write in MT table (new_iupred_result.txt; new_tango_result.txt)
2.SIFT and PolyPhen: use result file from tools directly written in MT table

part5:MySQL
1.python 11.create_Snpeffect_tables.py ==> connect MySQL database and create 3 empty tables.
2.python 12.insert_WT.py: input file('../result/tango_pfam.result.txt')
3.python 13.insert_MT.py: input file('../result/result_DDG.txt','new_iupred/tango_result.txt','SIFT && PolyPhen')
4.python 14.insert_C.py: input file('./result/info_ENSG_ENST_uniprot.txt','../result/info_snpid.txt')





