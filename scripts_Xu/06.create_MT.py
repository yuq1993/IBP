import pymysql

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect')

c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS MT""")
print("Creating MT table ....")
sql = """CREATE TABLE `MT` (
    `MT_id` int NOT NULL AUTO_INCREMENT,
    `ENST` char(15),
    `Chr` char(5),
    `g_pos` int,
    `AA_pos` int,
    `ref_AA` char(5),
    `alt_AA` char(5),
    `wt_IUPred` float,
    `mt_IUPred` float,
    `wt_Tango` float,
    `mt_Tango` float,
    `d_Tango` float,
    `Polyphen1` float,
    `Polyphen2` float,
    `Polyphen3` float,
    `Polyphen_effect` tinytext,
    `Sift1` float,
    `Sift2` float,
    `Sift_effect` tinytext,
    `PDBid` char(20),
    `chain` char(1),
    `PDB_pos` int,
    `DDG` float,
    PRIMARY KEY (`MT_id`)
    ) """
c.execute(sql)
print("Create MT table successful.")
