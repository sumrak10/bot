import sqlite3
 
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# sql = """ CREATE TABLE users
# 		(id_user text, ref_user text, iter_user text) """


# data = [('123243413', '10', '25')]
# sql = """INSERT INTO users
#          VALUES (?,?,?)"""

# cursor.executemany(sql, data)
# conn.commit()

# sql = "SELECT * FROM users WHERE id_user=?"
# cursor.execute(sql, [('123243413')])
# fetch_data = cursor.fetchall()
# fetch_data_reg = fetch_data[0]
# print(fetch_data_reg[2])

data = [('12', '254407586')]
sql = """UPDATE users 
		SET ref_user = ?
		WHERE id_user = ?"""
cursor.executemany(sql, data)
conn.commit()

conn.close()