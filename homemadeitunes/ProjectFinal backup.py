import mysql.connector
# import dbinit       

global bill
global playerCost
global item_bill

mydb = mysql.connector.connect(host='localhost', database='finaltest',
                               user='root', password='1234')
mycursor = mydb.cursor()

def registerCustomer():
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

def musictypeview():
    mycursor.execute("SELECT * FROM music_add")

    myresult = mycursor.fetchall()

    for x in myresult:
     print(x)
    
    ask = input("Do you want to hear some available samples? Y/N")
    if ask.lower() == 'y':
        import mp3play


def player_cost():
    global playerCost
    print("The following Players are available to all our customers:-")
    print("1. Astell & Kern A&ultima SP2000T at 3000$!")
    print("2. Onkyo DP-X1A at 1500$!")
    print("3. Apple iPod Touch (7th Generation) at 1800$!")
    print("4. SanDisk Clip Sport Plus at 1600$!")
    print("5. Sony NW 155L at 2000$!")
    x = int(input("Enter Your Choice "))
    n = int(input("Quantity? :"))
    if x == 1:
        print("You have opted for a Astell & Kern A&ultima SP2000T! The best MP3 player you can buy.")
        playerCost = 3000 * n
    elif x == 2:
        print("You have opted for an Onkyo DP-X1A! The best all-rounder MP3 player, ")
        playerCost = 1500 * n
    elif x == 3:
        print("You have opted for a Apple iPod Touch (7th Generation)! The best MP3 player for Apple lovers.")
        playerCost = 1800 * n
    elif x == 4:
        print("You have opted for a SanDisk Clip Sport Plus! ,The best MP3 player for sports")
        playerCost = 1600 * n
    elif x == 5:
        print("You have opted for a Sony NW 155L! ,The best MP3 player for hi-res audio on a budget")
        playerCost = 2000 * n
    else:
        print("Kindly choose a valid choice")
    print("Your cost is ", str(playerCost) + "$", "\n")


def music_cat():
    mycursor.execute("SELECT * FROM music_trend")

    myresult = mycursor.fetchall()

    for x in myresult:
     print(x)


def orderitem():
    global item_bill
    mycursor.execute("SELECT * FROM music_cat")

    myresult = mycursor.fetchall()

    for x in myresult:
     print(x)

    catchoice = int(input("Enter your choice of Album: "))
    if catchoice == 1:
        print("You have ordered Thriller")
        quantity = int(input("Enter quantity: "))
        item_bill = 42 * quantity
        print("Your amount for Thriller is",
              str(item_bill) + "$", "\n")
    elif catchoice == 2:
        print("You have ordered Back in Black!")
        quantity = int(input("Enter Quantity: "))
        item_bill = 50 * quantity
        print("Your amount for Back in Black is", str(item_bill) + "$", "\n")
    elif catchoice == 3:
        print("You have ordered The Bodyguard!")
        quantity = int(input("Enter quantity: "))
        item_bill = 68 * quantity
        print("Your amount for The Bodyguard is",
              str(item_bill) + "$", "\n")
    elif catchoice == 4:
        print("You have ordered The Darkside of the Moon!")
        quantity = int(input("Enter quantity: "))
        item_bill = 65 * quantity
        print("Your amount for The Darkside of the Moon is",
              str(item_bill) + "$", "\n")
    elif catchoice == 5:
        print("You have ordered Hotel California!")
        quantity = int(input("Enter quantity: "))
        item_bill = 15 * quantity
        print("Your amount for Hotel California is", str(item_bill) + "$",
              "\n")
    elif catchoice == 6:
        print(
            "You have ordered Led Zeppelin IV")
        quantity = int(input("Enter quantity: "))
        item_bill = 22 * quantity
        print("Your amount for Led Zeppelin IV "
              "factory in Paris is", str(item_bill) + "$", "\n")
    elif catchoice == 7:
        print("You have ordered Bad!")
        quantity = int(input("Enter quantity: "))
        item_bill = 22 * quantity
        print("Your amount for Bad is", str(item_bill) + "$",
              "\n")
    elif catchoice == 8:
        print("Metallica!")
        quantity = int(input("Enter quantity: "))
        item_bill = 30 * quantity
        print("Your amount for Metallica",
              str(item_bill) + "$", "\n")
    elif catchoice == 9:
        print("You have ordered Dangerous!")
        quantity = int(input("Enter quantity: "))
        item_bill = 25 * quantity
        print("Your amount for Dangerous is",
              str(item_bill) + "$", "\n")
    elif catchoice == 10:
        print(
            "You have ordered The Eminem Show")
        quantity = int(input("Enter quantity: "))
        item_bill = 42 * quantity
        print(
            "Your amount for The Eminem Show is",
            str(item_bill) + "$", "\n")
    else:
        print("Kindly Enter your choice from the given menu!")


def Instruments():
    bill = 0
    mycursor.execute("SELECT * FROM instrument")

    myresult = mycursor.fetchall()

    for x in myresult:
     print(x)

    numOfInstruments = int(input("Enter Quantity: "))

    quantity = input("Enter the quantity of your Instruments: ")
    if quantity.lower() == "Acoustic Guitar":
        bill = numOfInstruments * 7000
    elif quantity.lower() == "Keyboard":
        bill = numOfInstruments * 15000
    elif quantity.lower() == "Drums":
        bill = numOfInstruments * 17000
    elif quantity.lower() == "Bass Guitar":
        bill = numOfInstruments * 20000
    elif quantity.lower() == "Trumpet":
        bill = numOfInstruments * 2500
    elif quantity.lower() == "Violin":
        bill = numOfInstruments * 30000
    elif quantity.lower() == "Flute":
        bill = numOfInstruments * 3000
    else:
        print("Enter Valid choices!")
    print("Your bill is", bill, "\n")
    return bill


def lauBill():
    print(bill)


def resBill():
    print(item_bill)

def stayBill():
    print(playerCost)

def viewBill():
    cname = input("Enter Customer Name: ")
    print("Customer Name :", cname, "\n")
    print("Instrument bill:")
    print(bill)
    print("item bill:")
    print(item_bill)
    print("MP3 P1ayer Bill:")
    print(playerCost)
    print("Total Cost To Be Paid:",
          (bill+item_bill+playerCost))


def Menu():
    print("Press 1 to enter customer data.")
    print("Press 2 to view new addition to catalouge.")
    print("Press 3 to buy mp3 players.")
    print("Press 4 to view the trending albums")
    print("Press 5 to buy albums.")
    print("Press 6 to but instruments")
    print("Press 7 for the complete bill.")
    print("Press 8 to exit.")

    
    userinput = int(input("Enter your choice: "))
    if userinput == 1:
        registerCustomer()
    elif userinput == 2:
        musictypeview()
    elif userinput == 3:
        player_cost()
    elif userinput == 4:
        music_cat()
    elif userinput == 5:
        orderitem()
    elif userinput == 6:
        Instruments()
    elif userinput == 7:
        viewBill()
    elif userinput == 8:
        print('Have a nice day!!!')
        quit()
    else:
        print("Enter a suitable choice!")


def runagain():
    run = input("Do want to run the program again? Yes/No:")
    while run.lower() == 'yes'or 'y':
        Menu()
        run = input("Do want to run the program again? Yes/No:")


bill = 0
item_bill = 0
playerCost = 0

Menu()
runagain()
