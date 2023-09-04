
import mysql.connector as sql


con = sql.connect(host="localhost",password = "John3211",user="root") #connection object change your password

print("Bank Management System")

while True:
    password = input("Enter your password: ") #password to login to the bank system
    if password == "n": # you can change it here 
        print("Login successful")
        break
    else:
        print("Invalid password")

cur = con.cursor()


#below it creates a database if it doesn't exist and also creates the table if it doesn't exists
try:
    cur.execute("use bankdatabase")
except:
    cur.execute("create database bankdatabase") #the database name is bankdatabase
    cur.execute("use bankdatabase")
try:
    cur.execute("create table data(userid varchar(20) primary key,username varchar(20),balance int,interest decimal(10,2))") #this is the table you can edit it to add more fields
except:
    pass



while True:
    s = '''
1) Create new account
2) Delete existing account
3) Display an account
4) Exit
''' # you can add more features in this like edit an account , increaes or decrease the interest or balance etc
    print(s)
    choice = input("Choice: ")
    if not choice.isdigit() and choice in "1 2 3 4": #checks if the option is a number or not , also it cheks if its a valid number the "1 2 3 4" are the options you can add more to it like "1 2 3 4 5 6 7" and so on when you add more features
        print("Not a valid option")
        continue
    choice = int(choice)

    if choice == 1:

        userid = input("userid: ")
        username = input("username: ")
        balance = input("balance: ")
        interest =  input("interest: ")

        #checks wheather balance and interests are numbers 
        if not balance.isdigit() or not interest.isdigit():
            print("Balance or interest is not a number")
            continue

        try: #adding a new user
            cur.execute("INSERT INTO data values('{}', '{}',{},{})".format(userid,username,balance,interest))
            con.commit()
            print("Added new user")
        except:
            print("User id already exists")

    
    if choice == 2:

        userid = input("userid: ")

        try: #deleting a user
            cur.execute("delete from data where userid = '{}'".format(userid))
            con.commit()
            print("Deleted user")
        except:
            print("User id does not exist")
    if choice == 3:

        userid = input("userid: ")
        try: #displaying details of a specific user
            cur.execute("select * from data where userid = '{}'".format(userid))
            data = cur.fetchone()
            print("Userid: {},Username: {},Balance: {},Interest: {}".format(data[0],data[1],data[2],data[3]))#this just gets the data in the order of the table
        except:
            print("User id does not exists")

    if choice == 4:
        print("Saving...") #closing connections and breaking out of loop
        cur.close()
        con.close()
        print("Exiting...")
        break
         
    