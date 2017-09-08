import sqlite3
conn = sqlite3.connect('score.db')
curs = conn.cursor()
# curs.execute('''create table A
# (score INT)''')
ins = 'INSERT INTO A VALUES(?)'
# curs.execute(ins, (3,))
# curs.execute(ins, (4,))
curs.execute("select score from A")
print(curs.fetchall())

curs.execute('''create table B
(score INT)''')

curs.execute('''create table C
(score INT)''')

curs.close()
conn.close()