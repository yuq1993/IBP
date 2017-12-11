import pymysql

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect')

c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS coordinate""")
print("Creating coordinate table ....")
sql = """CREATE TABLE `coordinate` (
    `ID` int NOT NULL AUTO_INCREMENT,
    `Chr` char(5),
    `g_pos` int,
    `qual` float,
    `DP` tinytext,
    `Snpid` char(20),
    `ref_base` tinytext,
    `alt_base` tinytext,
    `ENSG` char(15),
    `ENST` char(15),
    `Uniprot` char(10),
    PRIMARY KEY (`ID`)
    ) """
c.execute(sql)
print("Create MT_protein table successful.")


conn.commit()
conn.close()
