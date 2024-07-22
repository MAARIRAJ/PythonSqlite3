import sqlite3

connection=sqlite3.connect("newdatabase.db")

print("Database opened")

connection.execute('''CREATE TABLE USERS(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL );''')

print("table created successfully")

connection.execute("INSERT INTO USERS (ID,NAME) VALUES (1,'PAUL')");
connection.execute("INSERT INTO USERS (ID,NAME) VALUES (2,'GEORGE')");
connection.execute("INSERT INTO USERS (ID,NAME) VALUES (3,'PETER')");
connection.execute("INSERT INTO USERS (ID,NAME) VALUES (4,'JOHNSON')");
connection.execute("INSERT INTO USERS (ID,NAME) VALUES (5,'MARI RAJ')");


connection.commit()

connection.close()