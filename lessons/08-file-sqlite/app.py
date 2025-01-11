import sqlite3
from ctypes import DEFAULT_MODE

con = sqlite3.connect('test1.db')
cur = con.cursor()



#cur.execute("CREATE TABLE user(name, year, title)")
# cur.execute('''
#         CREATE TABLE example1(
#        id INTEGER PRIMARY KEY,
#        name TEXT DEFAULT 'user',
#        age INTEGER DEFAULT 0,
#        title TEXT NOT NULL
#    );''')

# cur.execute('''INSERT INTO user (name, year, title)
#     VALUES ('Yasen PRO', '1999', 'User2345678910')
#     ;''')
# for i in range(100):
#     cur.execute('''INSERT INTO user (name, year, title)
#         VALUES (?,?,?)
#     ''', ('дмитрик', i, f'Школяр {i}'))
#
#     con.commit()

cur.execute("UPDATE user SET name='ТАРАС' WHERE year=0 ")
con.commit()
con.close()