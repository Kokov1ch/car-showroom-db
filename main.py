import sqlite3
# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("autosalon.sqlite")
cursor = con.cursor()
cursor.execute('''
SELECT * FROM Request
''')
print(cursor.fetchall())
# закрываем соединение с базой
con.close()