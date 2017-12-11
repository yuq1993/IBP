#insert info into MT table

import pymysql,re

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect',sql_mode='NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION')

c = conn.cursor()
#write SIFT data in WT table
Sift_file = open('../result/SIFTcleaned.txt','r')
lines = Sift_file.readlines()
for line in lines:
    if line != '\t\n':
        line = line.strip()
        line = line.split("\t")
        Chr = line[0].split(':')[0]
        ENST = line[1]
        pos = int(line[0].split(':')[1])
        AA_pos = int(line[4])
        ref_AA = line[2]
        alt_AA = line[3]
        if line[5] == 'NA':
            Sift1 = Sift2 = -1
        else:
            Sift1 = float(line[5])
            Sift2 = float(line[6])
        Sift_effect = line[7]
        sql = "INSERT INTO MT(ENST,Chr,g_pos,AA_pos,ref_AA,alt_AA,Sift1,Sift2,Sift_effect) VALUES ('%s','%s','%d','%d','%s','%s','%f','%f','%s')" % (ENST,Chr,pos,AA_pos,ref_AA,alt_AA,Sift1,Sift2,Sift_effect)
        c.execute(sql)
Sift_file.close()

#write polyphen data:
Polyphen_file = open('../result/polyphenClean.txt','r')
line = Polyphen_file.readline()
while line != '':
    line = line.strip()
    line = line.split("\t")
    Chr = line[0].split(':')[0]
    pos = int(line[0].split(':')[1])
    if line[1].strip() =='?':
        P1 = P2 = P3 = -1
    else:
        P1 = float(line[1])
        P2 = float(line[2])
        P3 = float(line[3])
    Pe = line[4].strip()
    sql_select = """SELECT * FROM MT where Chr = '%s' and g_pos= '%d' """ %(Chr,pos)
    n = c.execute(sql_select)
    if n > 0:
        sql_update = """UPDATE MT set Polyphen1 = '%f',Polyphen2 = '%f',Polyphen3 = '%f',Polyphen_effect = '%s' where g_pos = '%d' """ % (P1,P2,P3,Pe,pos)
        c.execute(sql_update)
    else:
        sql_insert = """INSERT INTO mt(Chr,g_pos,Polyphen1,Polyphen2,Polyphen3,Polyphen_effect) values ('%s','%d','%f','%f','%f','%s')""" % (Chr,pos,P1,P2,P3,Pe)
        c.execute(sql_insert)
    line = Polyphen_file.readline()
Polyphen_file.close()

#write DDG:
foldx_file = open('../result/result_DDG.txt','r')
line = foldx_file.readline()
while line != '':
    line = line.strip()
    line = line.split("\t")
    Chr = line[0]
    g_pos = int(line[1])
    ENST = line[2]
    PDBid = line[3]
    alt_AA = line[4]
    chain = line[5]
    PDB_pos = int(line[6])
    ref_AA = line[7]
    DDG = float(line[8])
    sql_select = """SELECT * FROM MT where ENST = '%s' and g_pos= '%d' """ %(ENST,g_pos)
    n = c.execute(sql_select)
    if n > 0:
        sql_update = """UPDATE MT set PDBid = '%s',chain = '%s',PDB_pos = '%d',DDG ='%f' where ENST = '%s' """ % (PDBid,chain,PDB_pos,DDG,ENST)
        c.execute(sql_update)
    else:
        sql_insert = """INSERT INTO MT(ENST,Chr,g_pos,ref_AA,alt_AA,PDBid,chain,PDB_pos,DDG) values ('%s','%s','%d','%s','%s','%s','%s','%d','%f')""" % (ENST,Chr,g_pos,ref_AA,alt_AA,PDBid,chain,PDB_pos,DDG)
        c.execute(sql_insert)
    #sql = "UPDATE MT set (Polyphen1='%f',Polyphen2='%f',Polyphen3='%f',Polyphen_effect='%s') where Position='%d'"
    line = foldx_file.readline()
foldx_file.close()

#write IUPred:
iupred_file = open('../result/new_iupred_result.txt','r')
line = iupred_file.readline()
while line != '':
    line = line.strip()
    info = re.split('\s+',line)
    Chr = info[0]
    pos = int(info[1])
    ENST = info[2]
    AA_pos = int(info[3])
    wt_I = float(info[4])
    mt_I = float(info[5])
    sql_select = """SELECT * FROM MT where ENST = '%s' and g_pos= '%d' """ %(ENST,pos)
    n = c.execute(sql_select)
    if n > 0:
        sql_update = """UPDATE MT set wt_IUPred = '%f',mt_IUPred = '%f' where ENST = '%s' and g_pos = '%d' """ % (wt_I,mt_I,ENST,pos)
        c.execute(sql_update)
    else:
        sql_insert = """INSERT INTO mt(ENST,Chr,g_pos,wt_IUPred,mt_IUPred,AA_pos) values ('%s','%s','%d','%f','%f','%d')""" % (ENST,Chr,pos,wt_I,mt_I,AA_pos)
        c.execute(sql_insert)
    line = iupred_file.readline()
iupred_file.close()

# write tango:
tango_file = open('../result/new_tango_result.txt','r')
line = tango_file.readline()
while line != '':
    line = line.strip()
    info = re.split('\s+',line)
    Chr = info[0]
    pos = int(info[1])
    ENST = info[2]
    wt_T = float(info[3])
    mt_T = float(info[4])
    d_T = float(info[5])
    sql_select = """SELECT * FROM MT where ENST = '%s' and g_pos= '%d' """ %(ENST,pos)
    n = c.execute(sql_select)
    if n > 0:
        sql_update = """UPDATE MT set wt_Tango = '%f',mt_Tango = '%f',d_Tango ='%f' where ENST = '%s' and g_pos = '%d' """ % (wt_T,mt_T,d_T,ENST,pos)
        c.execute(sql_update)
    else:
        sql_insert = """INSERT INTO mt(ENST,Chr,g_pos,wt_Tango,mt_Tango,d_Tango) values ('%s','%s','%d','%f','%f','%f')""" % (ENST,Chr,pos,wt_T,mt_T,d_T)
        c.execute(sql_insert)
    line = tango_file.readline()
tango_file.close()

conn.commit()
conn.close()
