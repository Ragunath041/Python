import sqlite3
connection = sqlite3.connect("Academy.db")
cursor = connection.cursor()
sql_command = '''create table Student(f_name , l_name , DOB)'''


datas = [
    ("a" , "A" , "21-11-2003"),
    ("b" , "B" , "21-11-2004"),
    ("c" , "C" , "21-11-2005"),
    ("d" , "D" , "21-11-2006")
]
for i in datas:
    format_str = '''INSERT INTO Student(f_name , l_name , DOB)
                    VALUES(NULL,"{}")'''
cursor.execute(sql_command)
