import pymysql,re

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect',sql_mode='NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION')

c = conn.cursor()
#write ENST_ENSG_snpid data in WT table
c_file = open('../result/info_ENSG_ENST_uniprot.txt','r')
snp_file = open('../result/info_snpid.txt','r')

line = c_file.readline()
while line != '':
    line = line.strip()
    info = re.split('\s+',line)
    Chr = info[0]
    pos = int(info[1])
    ref_b = info[2]
    alt_b = info[3]
    qual = float(info[4])
    DP = info[5]
    ENSG = info[6]
    ENST = info[7]
    if len(info) < 9:
        gene = 'NA'
        Uniprot = 'NA'
    else:
        gene = info[8]
        uniprot = info[9]
    sql = "INSERT INTO coordinate(Chr,g_pos,qual,DP,ref_base,alt_base,gene,ENSG,ENST,Uniprot) VALUES ('%s','%d','%f','%s','%s','%s','%s','%s','%s','%s')" % (Chr,pos,qual,DP,ref_b,alt_b,gene,ENSG,ENST,uniprot)
    c.execute(sql)
    line = c_file.readline()

snp_line = snp_file.readline()
while snp_line !='':
    line = snp_line.strip().split('\t')
    Chr = line[0]
    pos = int(line[1])
    snpid = line[2]
    sql_update = """UPDATE coordinate set Snpid = '%s' where Chr = '%s' and g_pos = '%d' """ % (snpid,Chr,pos)
    c.execute(sql_update)
    snp_line = snp_file.readline()


conn.commit()
conn.close()
