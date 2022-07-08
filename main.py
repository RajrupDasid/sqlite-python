import sqlite3

connection=sqlite3.connect("linux.db")

cursor=connection.cursor()
cursor.execute("create table linux (release_year, release_name, version)")
release_list=[
            (1991,"Linux Kernel","1.00"),
            (1992,"Linux kernel 2","2.00"),
            (2021,"Linux Zen","5.12"),
            (2022,"Linux zen extra",5.19),
        ]

cursor.executemany("insert into linux values(?,?,?)",release_list)
for row in cursor.execute("select * from linux"):
    print(row)
#print specific versions
cursor.execute("select * from linux where version=:v",{"v":"2.00"})
linux_search=cursor.fetchall()
print(linux_search)

cursor.execute("create table system (name,dist)")
cursor.execute("insert into system values (?,?)",("arch","arch"))
















connection.close()


