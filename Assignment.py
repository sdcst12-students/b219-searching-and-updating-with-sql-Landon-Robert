import sqlite3

#part 1

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = """
create table if not exists customers4 (
    Uid integer primary key autoincrement,
    fname tinytext,
    lname tinytext,
    phone bigint,
    email tinytext,
    address tinytext,
    city tinytext, 
    postalcode tinytext);
"""
cursor.execute(query)

q2 = """
create table if not exists pets (
    Pid integer primary key autoincrement,
    name tinytext,
    type tinytext,
    breed tinytext,
    birthdate tinytext,
    ownerID int);
"""
cursor.execute(q2)

q3 = """
create table if not exists visits (
    Vid integer primary key autoincrement,
    ownerid int,
    petid int,
    details text,
    cost float(16,2),
    paid float(16,2));
"""
cursor.execute(q3)

end = False
while end == False:
    option = input("\nWhat would you like to do?\nExit: 0\nAdd new customer: 1\nSearch for a customer: 2\n")
    if option == "0":
        end = True
    elif option == "1":
        print("Please enter relevant customer information:")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        phone = int(input("Phone Number (no spaces): "))
        email = input("Email:")
        address = input("Address: ")
        city = input("City: ")
        postalcode = input("Postal Code: ")
        query = f"insert into customers4 (fname,lname,phone,email,address,city,postalcode) values ('{fname}','{lname}','{phone}','{email}','{address}','{city}','{postalcode}');"
        print(query)
        cursor.execute(query)
    elif option == "2":
        userInfo = ["Uid", "fname", "lname", "phone", "email", "address", "city", "postalcode"]
        decision = int(input("Search for existing customer by:\nUid: 1\nFirst Name: 2\nLast Name: 3\nPhone Number: 4\nEmail: 5\nAddress: 6\nCity: 7\nPostal Code: 8\nExit: 0\n"))
        if int(decision) == 0:
            end = True
        elif 1 <= int(decision) <= 8:
            Uinfo = input("Please enter the corresponding info (ex. if you chose name, enter name): ")
            cursor.execute(f"select * from customers4 where {userInfo[decision-1]}='{Uinfo}'")
            print(cursor.fetchall())
        else:
            print("That is not a valid input.")
    else: 
        print("That is not a valid input.")

#part 2

end2 = False
while end2 == False:
    option = input("\nWhat would you like to do?\nExit: 0\nID: 1\nData: 2\n")
    if option == 0:
        end2 = False
    elif option == 1:
        searchId = input("Enter Uid: ")
    
