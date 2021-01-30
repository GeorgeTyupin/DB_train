import sqlite3
 
db = sqlite3.connect("computer_shop.db")
cur = db.cursor()

#sql = "SELECT * FROM Comps"
#print(cur.execute(sql).fetchall())

sql = '''
INSERT INTO Comps
(Model , Processor , Price , Count)
VALUES ("Asus" , "i5" , 74000 , 15 )
'''
cur.execute(sql)
db.commit()
