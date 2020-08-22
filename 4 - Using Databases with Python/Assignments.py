# Assignment: Our First Database
# Execute following SQL commands on SQLite browser

# CREATE TABLE Ages ( 
#   name VARCHAR(128), 
#   age INTEGER
# )

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Bryce', 19);
# INSERT INTO Ages (name, age) VALUES ('Domhnall', 37);
# INSERT INTO Ages (name, age) VALUES ('Adelaide', 23);
# INSERT INTO Ages (name, age) VALUES ('Unity', 20);
# INSERT INTO Ages (name, age) VALUES ('Turki', 30);
# INSERT INTO Ages (name, age) VALUES ('Kiyara', 16);

# SELECT hex(name || age) AS X FROM Ages ORDER BY X
################################################################################
# # Assignment: Counting Email in a Database
# import sqlite3

# conn = sqlite3.connect('orgdb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# i = 0
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1].split('@')
#     org = email[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (org,))
#     i += 1
#     if i % 100 == 0:
#         conn.commit()
# conn.commit()
# # print(i)
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()
################################################################################
# Assignment: Multi-Table Database - Tracks
# THIS ASSIGNMENT IS ON ~/tracks/tracks.py file
################################################################################
# # Assignment: Many Students in Many Courses
# import json
# import sqlite3

# conn = sqlite3.connect('rosterdb.sqlite')
# cur = conn.cursor()

# Do some setup
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;

# CREATE TABLE User (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# str_data = open(fname).read()
# json_data = json.loads(str_data)
# i = 0
# for entry in json_data:

#     name = entry[0]
#     title = entry[1]
#     role = entry[2]

#     print((name, title, role))

#     cur.execute('''INSERT OR IGNORE INTO User (name)
#         VALUES ( ? )''', ( name, ) )
#     cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
#     user_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Course (title)
#         VALUES ( ? )''', ( title, ) )
#     cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
#     course_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Member
#         (user_id, course_id, role) VALUES ( ?, ?, ? )''',
#         ( user_id, course_id, role ) )

#     i += 1
#     if i % 100 == 0:
#         conn.commit()
# conn.commit()

# Assignment: Databases and Visualization (peer-graded)
# THIS ASSIGNMENT IS ON ~/geodata/ files