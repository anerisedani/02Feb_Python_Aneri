import sqlite3

db=sqlite3.connect("task1.db")
print("database connected!")

#create table
create_tbl="create table studinfo(id integer primary key autoincrement, name text, city text)"
db.execute(create_tbl)
print("table created")
