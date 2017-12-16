import pymysql

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect')

c = conn.cursor()

#create coordinate table
'''c.execute("""DROP TABLE IF EXISTS Coordinate""")
print("Creating Coordinate table ....")
sql = """CREATE TABLE `Coordinate` (
    `ID` int NOT NULL AUTO_INCREMENT,
    `Chr` char(5),
    `g_pos` int,
    `Qual` float,
    `DP` tinytext,
    `Snpid` char(20),
    `ref_base` tinytext,
    `alt_base` tinytext,
    `Gene` tinytext,
    `ENSG` char(15),
    `ENST` char(15),
    `Uniprot` char(10),
    PRIMARY KEY (`ID`)
    ) """
c.execute(sql)
print("Create Coordinate table successful.")

#create wt table
c.execute("""DROP TABLE IF EXISTS WT""")
#may need to change this: if this table exist, update it otherwise create new??
print("Creating wt_pfam table ....")
sql = """CREATE TABLE `WT` (
    `wt_id` int NOT NULL AUTO_INCREMENT,
    `ENST` char(15),
    `start_pos` int,
    `end_pos` int,
    `hmm_name` varchar(20),
    `hmm_type` varchar(10),
    `Tango` float,
    PRIMARY KEY (`wt_id`)
    ) """
c.execute(sql)
print("Create WT table successful.")'''

#create mt table
c.execute("""DROP TABLE IF EXISTS MT""")
print("Creating MT table ....")
sql = """CREATE TABLE `MT` (
    `ENST` char(15),
    `g_pos` int,
    `Chr` char(5),
    `AA_pos` int,
    `ref_AA` char(5),
    `alt_AA` char(5),
    `wt_IUPred` float,
    `mt_IUPred` float,
    `wt_Tango` float,
    `mt_Tango` float,
    `d_Tango` float,
    `pph_prob` float,
    `pph_FPR` float,
    `pph_TPR` float,
    `Polyphen_effect` tinytext,
    `Sift_score` float,
    `Sift_median` float,
    `Sift_effect` tinytext,
    `PDBid` char(20),
    `chain` char(1),
    `PDB_pos` int,
    `DDG` float,
    PRIMARY KEY (`ENST`,`g_pos`)
    ) """
c.execute(sql)
print("Create MT table successful.")



