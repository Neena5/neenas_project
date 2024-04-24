import sqlite3


con=sqlite3.connect('stud.db')
con.execute("""create table student(
            id integer primary key autoincrement,name text not null,email text,phone integer)""")



con.close()

