# input file: iupred_result.txt(from Qian's script) ==> new_iupred_reuslt_txt for mysql
# input file: tango_result.txt(from Qian's script) ==> new_tango_reuslt_txt for mysql


grep -v ERROR ../result/iupred_result.txt | cut -f -1,2,10,17-19 > ../result/new_iupred_result.txt

grep -v ERROR ../result/tango.results.txt | cut -f -1,2,10,17-19 > ../result/new_tango_result.txt

