import pymysql

conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect')

c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS wt_pfam""")
#may need to change this: if this table exist, update it otherwise create new??
print("Creating wt_pfam table ....")
sql = """CREATE TABLE `wt_pfam` (
    `wt_pfam_id` int NOT NULL AUTO_INCREMENT,
    `ENST` char(15) NOT NULL,
    `start_pos` int,
    `end_pos` int,
    `hmm_name` varchar(20),
    `hmm_type` varchar(10),
    PRIMARY KEY (`wt_pfam_id`)
    ) """
c.execute(sql)
print("Create wt_pfam table successful.")

