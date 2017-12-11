#insert info into WT table

import pymysql

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect',sql_mode='NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION')

c = conn.cursor()
#write example data in WT table
with open('pfam_ENST_table.txt','r') as ENST_file:
    for line in ENST_file:
        line = line.strip()
        line = line.split("\t")
        ENST = line[0]
        start_pos = int(line[1])
        end_pos = int(line[2])
        hmm_name = line[3]
        hmm_type = line[4]
        sql = "INSERT INTO WT_pfam(ENST,start_pos,end_pos,hmm_name,hmm_type) VALUES ('%s','%d','%d','%s','%s')" % (ENST,start_pos,end_pos,hmm_name,hmm_type)
        '''try:
            c.execute(sql)
            conn.commit()
        except:
            conn.rollback()'''
        c.execute(sql)

conn.commit()
conn.close()
