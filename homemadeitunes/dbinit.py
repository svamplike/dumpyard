import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                               user='root', password='1234')
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE finaltest")
mycursor.execute("use finaltest")
mydb.commit()
def dbin():
    mycursor.execute("CREATE TABLE customer_data (name VARCHAR(255),addr VARCHAR(255) ,DateBir Date,phn Varchar(20))")
    mycursor.execute("CREATE TABLE music_trend (SrNo VARCHAR(255), Artist VARCHAR(255), Name VARCHAR(255), Genre VARCHAR(255), Length VARCHAR(255))")
    mycursor.execute("CREATE TABLE music_cat (SrNo VARCHAR(255), Artist VARCHAR(255), Name VARCHAR(255), Genre VARCHAR(255), Length VARCHAR(255))")
    mycursor.execute("CREATE TABLE music_add (SrNo VARCHAR(255), Artist VARCHAR(255), Name VARCHAR(255), Genre VARCHAR(255), Length VARCHAR(255))")
    mycursor.execute("CREATE TABLE Instrument (SrNo VARCHAR(255), Class VARCHAR(255), Company VARCHAR(255), Year VARCHAR(255), Price VARCHAR(255))")
    mydb.commit()










    
def CreateTable():
    
    
    
    
    
    customer = []
    name = input("Enter the Name of the Customer: ")
    customer.append(name)
    addr = input("Enter Address: ")
    customer.append(addr)
    DateBir = input("Enter DOB : ")
    customer.append(DateBir)
    phn = input("Enter Phone no.: ")
    customer.append(phn)
    customer_Data = (customer)
    sql_command = 'insert into customer_data(name,addr,DateBir,phn) values (%s,%s,%s,%s)'
    mycursor.execute( sql_command, customer_Data)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")


def CreateTable2():
 mycursor = mydb.cursor()
 
 sql = "INSERT INTO music_add (SrNo , Artist , Name , Genre , Length ) VALUES (%s, %s,%s,%s,%s)"
 val = [
  ('1', 'Michael Jackson', 'Thriller', 'Pop, post-disco, funk, rock'  , '42:16'),
  ('2', 'AC/DC'  , 'Back in Black', 'Hard rock' , ' 42:11'),
  ('3', 'Whitney Houston / various artists' , 'The Bodyguard', 'R&B, soul, pop, soundtrack', ' 57:44'),
  ('4', 'Pink Floyd' , 'The Dark Side of the Moon', 'Progressive rock', ' 42:50'),
  ('5', 'Eagles' , 'Hotel California', 'Soft rock', ' 43:28'),
  ('6', 'Led Zeppelin' , 'Led Zeppelin IV', 'Hard rock, heavy metal, folk rock	', ' 42:20'),
  ('7', 'Michael Jackson' , 'Bad', 'Pop, rhythm and blues, funk and rock', ' 48:40 '),
  ('8', 'Metallica' , 'Metallica', 'Heavy metal', ' 62:40'),
  ('9', 'Michael Jackson' , 'Dangerous', 'New jack swing, R&B and pop	', ' 77:03'),
  ('10', 'Eminem' , 'The Eminem Show', 'Hip hop', ' 77:19'),
  
    ]

 mycursor.executemany( sql, val)
 mydb.commit()
 print(mycursor.rowcount, "record was inserted.")

def CreateTable3():
 mycursor = mydb.cursor()
 sql = "INSERT INTO music_trend (SrNo , Artist ,Name , Genre , Length ) VALUES (%s,%s,%s,%s,%s)"
 val = [
  ('1', 'Michael Jackson', 'Thriller', 'Pop, post-disco, funk, rock'  , '42:16'),
  ('2', 'AC/DC'  , 'Back in Black', 'Hard rock' , ' 42:11'),
  ('3', 'Whitney Houston / various artists' , 'The Bodyguard', 'R&B, soul, pop, soundtrack', ' 57:44'),
  ('4', 'Pink Floyd' , 'The Dark Side of the Moon', 'Progressive rock', ' 42:50'),
  ('5', 'Eagles' , 'Hotel California', 'Soft rock', ' 43:28'),
  
    ]

 mycursor.executemany( sql, val)
 mydb.commit()
 print(mycursor.rowcount, "record was inserted.")

def CreateTable4():
 mycursor = mydb.cursor()
 sql = "INSERT INTO music_cat (SrNo ,Artist,Name , Genre , Length ) VALUES (%s, %s,%s,%s,%s)"
 val = [
  ('1', 'Michael Jackson', 'Thriller', 'Pop, post-disco, funk, rock'  , '42:16'),
  ('2', 'AC/DC'  , 'Back in Black', 'Hard rock' , ' 42:11'),
  ('3', 'Whitney Houston / various artists' , 'The Bodyguard', 'R&B, soul, pop, soundtrack', ' 57:44'),
  ('4', 'Pink Floyd' , 'The Dark Side of the Moon', 'Progressive rock', ' 42:50'),
  ('5', 'Eagles' , 'Hotel California', 'Soft rock', ' 43:28'),
  ('6', 'Led Zeppelin' , 'Led Zeppelin IV', 'Hard rock, heavy metal, folk rock	', ' 42:20'),
  ('7', 'Michael Jackson' , 'Bad', 'Pop, rhythm and blues, funk and rock', ' 48:40 '),
  ('8', 'Metallica' , 'Metallica', 'Heavy metal', ' 62:40'),
  ('9', 'Michael Jackson' , 'Dangerous', 'New jack swing, R&B and pop	', ' 77:03'),
  ('10', 'Eminem' , 'The Eminem Show', 'Hip hop', ' 77:19'),
  
    ]

 mycursor.executemany( sql, val)
 mydb.commit()
 print(mycursor.rowcount, "record was inserted.")


def CreateTable5():
 mycursor = mydb.cursor()
 sql = "INSERT INTO Instrument (SrNo , Class , Company , Year , Price ) VALUES (%s, %s,%s,%s,%s)"
 val = [
  ('1', 'Acoustic Guitar' , 'Taylor', '2021'  , ' 7000'),
  ('2', 'Keyboard'  , 'Yamaha', '2019' , ' 15000'),
  ('3', 'Drums' , 'Tama', '2022', ' 17000'),
  ('4', 'Bass Guitar' , 'Epiphone', '2020', ' 20000'),
  ('5', 'Trumpet' , 'Vincent Bach', '2017', ' 2500'),
  ('6', 'Violin' , 'Stentor', '2018', ' 30000'),
  ('7', 'Flute' , 'Muramatsu', '2020', ' 3000'),
  
  
    ]

 mycursor.executemany(sql, val)
 mydb.commit()
 print(mycursor.rowcount, "record was inserted.")


dbin()
CreateTable2()


CreateTable3()
CreateTable4()

CreateTable5()




