import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                               user='root', password='1234')
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE manpy")
mycursor.execute("use manpy")
mydb.commit()



mycursor.execute("SELECT * FROM instrument")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
