import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="a1b2c3d4",
    database="abacom"
)

cursor = midb.cursor()
# cursor.execute("select * from usuario")
# cursor.execute("select * from usuario limit 3")
# # sql = "insert into usuario(email, username, edad) values (%s, %s, %s)"
sql = "update usuario set email = %s where edad = %s"
# sql = "delete from usuario where edad = %s"
# values = ("usuario4@gmail.com", "usuario004", "20")
values = ("usuariofinal001@gmail.com","45")
# values = (33,)

cursor.execute(sql, values)
midb.commit()
# resultado = cursor.fetchall()
# resultado = cursor.fetchone()

# print(cursor.rowcount)
# print(resultado)
