#To create the SNPeffect database

import pymysql


conn = pymysql.connect(host='localhost', user='root',password='123456',db='SNPeffect')

c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS coordinate""")
#may need to change this: if this table exist, update it otherwise create new??
print("Creating coordinate table ....")
sql = """CREATE TABLE `coordinate` (
`id` int NOT NULL AUTO_INCREMENT,
`Snpid` char NOT NULL,
`chr` char NOT NULL,
`position` int NOT NULL,
`ref_base` char NOT NULL,
`alt_base` char NOT NULL,
`ENSG` char NOT NULL,
`ENST` char NOT NULL,
`ref_codon` char NOT NULL,
`alt_codon` char NOT NULL,
`Uniprot` char NOT NULL,
`PDBid` char NOT NULL,
PRIMARY KEY (`id`)
) """
#FOREIGN KEY (`PDBid`) REFERENCES MT_PDB (`PDBid`)，
#FOREIGN KEY (`uniprot`) REFERENCES MT_Protein (`uniprot`)
c.execute(sql)
print("Create coordinate table successful.")

c.execute("""DROP TABLE IF EXISTS mt_pdb""")
print("Creating MT_pdb table ....")
sql = """CREATE TABLE `mt_pdb` (
`MT_PDBid` int NOT NULL AUTO_INCREMENT,
`Uniprot` char(10) NOT NULL,
`PDBid` char(10) NOT NULL,
`chain` char NOT NULL,
`position` int NOT NULL,
`ref_AA` char NOT NULL,
`alt_AA` char NOT NULL,
`ddG` float NOT NULL,
PRIMARY KEY (`MT_PDBid`)
) """
#FOREIGN KEY (`PDBid`) REFERENCES COORDINATE (`PDBid`)
c.execute(sql)
print("Create mt_pdb table successful.")


c.execute("""DROP TABLE IF EXISTS MT_protein""")
print("Creating MT_protein table ....")
sql = """CREATE TABLE `mt_protein` (
`MT_Proteinid` int NOT NULL AUTO_INCREMENT,
`Uniprot` char NOT NULL,
`Position` int NOT NULL,
`ref_AA` char NOT NULL,
`alt_AA` char NOT NULL,
`Tango` float NOT NULL,
`Polyphen` float NOT NULL,
`Sift` float NOT NULL,
PRIMARY KEY (`MT_Proteinid`)
) """
#FOREIGN KEY (`Uniprot`) REFERENCES COORDINATE (`Uniprot`)
c.execute(sql)
print("Create mt_pdb table successful.")

print("Creating WT table ....")
sql = """CREATE TABLE `wt` (
`WTid` int NOT NULL AUTO_INCREMENT,
`Uniprot` char NOT NULL,
`length` int NOT NULL,
`Pfam` char NOT NULL,
`Tango` float NOT NULL,
`IUPred` float NOT NULL,
PRIMARY KEY (`WTid`)
) """
#FOREIGN KEY (`Uniprot`) REFERENCES COORDINATE (`Uniprot`)
c.execute(sql)
print("Create mt_pdb table successful.")

#write toy example data in MT_PDB table
with open('MT_PDB_table.txt','r') as MT_PDBfile:
    for line in MT_PDBfile:
        line = line.strip()
        line = line.split("\t")
        Uniprot = line[0]
        PDBid = line[1]
        chain = line[2]
        position = int(line[3])
        ref_AA = line[4]
        alt_AA = line[5]
        ddG = float(line[6])
        sql = "INSERT INTO MT_PDB(UNIPROT,PDBID,CHAIN,POSITION,REF_AA,ALT_AA,DDG) VALUES ('%s','%s','%s','%d','%s','%s','%d')" % (Uniprot,PDBid,chain,position,ref_AA,alt_AA,ddG)

        try:
            c.execute(sql)
            conn.commit()
        except:
            conn.rollback()


conn.close()
