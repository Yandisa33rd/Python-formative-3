from tableclass import Table

def UsernameFunction(Username, Password, TableList):
    File = open(r"Text File\Login.txt", 'r')

    for line in File:
        TempArr = line.split(",")
        Pass = TempArr[1].strip("\n")
        if Pass == Password:
            if Username == TempArr[0]:
                print("\nLogging in\n")
                File.close()
                return True
            else:
                break  # Exit the loop if username doesn't match

    File.close()  # Move the file close statement here to close after the loop completes
    print("Those Credintials don't match our records \n ")
    return False

def assignTableToWaiter(Username, TableList):
    print("\nCurrent available tables")
    print("Enter 0 to return to Main Menu")

    count = 0
    for x in TableList:
        if x.waiter == "Undefined":
            print(f" * Table {x.number} ")
            count += 1

    if count == 0:
        print("\nThere are no avaiable tables. Returning to main menu.\n")
        main(Username, TableList)
    
    TableChoice = input("What table are you going to use: ")

    if TableChoice == "1" or TableChoice == "2" or TableChoice == "3" or TableChoice == "4" or TableChoice == "5" or TableChoice == "6" or TableChoice == "7":
        TableChoice = int(TableChoice)
        TableChoice -= 1
        tableChosen = TableList[TableChoice]
        if tableChosen.IsAssigned():
            tableChosen.assignWaiter(Username)
            tableChosen.assigned = True

            print(f'Waiter for Table {tableChosen.number} is now {tableChosen.waiter}')
            print()
            AddCustomers(Username, TableList)


        else:
            print(f"\nTable is assigned to {tableChosen.waiter}")
            print("please choose an availlable table\n")
            assignTableToWaiter(Username,TableList)
    elif TableChoice == "0":
        main(Username,TableList)
    else:
        print('That value is not in our system')
        assignTableToWaiter(Username,TableList)

def AddCustomers(Username,TableList):
    choice = input("would you like to add customers y/n: ")
    if choice == "y":
        tempArr = []
        count = 1
        print()
        print(f"These are the Tables assigned to {Username}")

        for x in TableList:
            if x.waiter == Username:
                tempArr.append(x)
                print(f'{count}: Table {x.number}')
                count += 1

        TableChoice = input("Choose a table: ")

        try:
            TableChoice = int(TableChoice)
            TableChoice -= 1

            if TableChoice >= 0 and TableChoice < len(tempArr):
                tableChosen = tempArr[TableChoice]
                customerNumber = input("How many customers to add: ")
                try:
                    customerNumber = int(customerNumber)
                    tableChosen.add_customer(customerNumber)
                    print(f"This table now has {tableChosen.customers} ")
                    print()
                    main(Username, TableList)

                except ValueError:
                    print(f"DebUgger: Error: Cannot convert '{customerNumber}' to an integer. Rerunning Fuction")
                    AddCustomers(Username,TableList)
            else:
                print("That is not an acceptable answer")
                AddCustomers(Username,TableList)

        except ValueError:
            print(f"DebUgger: Error: Cannot convert '{TableChoice}' to an integer. Rerunning Fuction")
            AddCustomers(Username,TableList)

    elif choice == "n":
        main(Username,TableList)

    else:
        print('That value is not in our system')
        AddCustomers(Username,TableList)
        
def ChangeCustomers(Username,TableList):
    Arrcounter = 0
    for x in TableList:
        if x.waiter == Username:
            Arrcounter += 1

    if Arrcounter == 0:
        print("\nThere are no avaiable tables. Returning to main menu.\n")
        main(Username, TableList)

    choice = input("Would you like to Change customers y/n: ")


    if choice == "y":
        tempArr = []
        count = 1
        print()
        print(f"These are the Tables assigned to {Username}")

        for x in TableList:
            if x.waiter == Username:
                tempArr.append(x)
                print(f'{count}: Table {x.number}')
                count += 1

        TableChoice = input("Choose a table: ")

        try:
            TableChoice = int(TableChoice)
            TableChoice -= 1

            if TableChoice >= 0 and TableChoice < len(tempArr):
                tableChosen = tempArr[TableChoice]
                customerNumber = input("What value do you want us to change it to: ")
                try:
                    customerNumber = int(customerNumber)
                    tableChosen.add_customer(customerNumber)
                    print(f"This table now has {tableChosen.customers} ")
                    print()
                    main(Username, TableList)

                except ValueError:
                    print(f"DebUgger: Error: Cannot convert '{customerNumber}' to an integer. Rerunning Fuction")
                    ChangeCustomers(Username,TableList)
            else:
                print("That is not an acceptable answer")
                ChangeCustomers(Username,TableList)

        except ValueError:
            print(f"DebUgger: Error: Cannot convert '{TableChoice}' to an integer. Rerunning Fuction")
            ChangeCustomers(Username,TableList)

    elif choice == "n":
        main(Username,TableList)

    else:
        print('That value is not in our system')
        ChangeCustomers(Username,TableList)

def AddOrder(Username,TableList):
        tempArr = []
        print()

        count = 1
        print(f"These are the Tables assigned to User: {Username}")
        for x in TableList:
            if x.waiter == Username:
                tempArr.append(x)
                print(f'{count}: Table {x.number}')
                count += 1

        if len(tempArr) == 0:
            print(f"There are no Tables asigned to User: {Username}")
            main(Username, TableList)

        TableChoice = input("Choose a table: ")
        try:
            TableChoice = int(TableChoice)
            TableChoice -= 1

            if TableChoice >= 0 and TableChoice < len(tempArr):
                tableChosen = tempArr[TableChoice]    
                print(f"Table chosen is {tableChosen.number}")
                LoadorderMenu(Username,TableList,tableChosen)

            else:
                print("That is not an acceptable answer")
                AddOrder(Username,TableList)

        except ValueError:
            print(f"DebUgger: Error: Cannot convert '{TableChoice}' to an integer. Rerunning Fuction")
            AddOrder(Username,TableList)
               
def LoadorderMenu(Username, TableList, TableChoice):
    File = open(r"Text File\Stock.txt", 'r')
    Foodlist = []
    Pricelist = []

    for line in File:
        temp_arr = line.split(",")
        item = temp_arr[0]
        Foodlist.append(item)

        price = temp_arr[1].strip()
        Pricelist.append(price)

    File.close()  # Close the file before reopening

    File = open(r"Text File\Stock.txt", 'r')

    counter = 1

    for line in File:
        TempArr2 = line.split(",")
        print(f"{counter}: {TempArr2[0]} Price:{TempArr2[1].strip()}")
        counter += 1

    File.close()

    orderchoice = input("What pick an order to add: ")
    try:
        orderchoice = int(orderchoice)
        if orderchoice >= 0 and orderchoice < 12:
            orderchoice -= 1
            Choice = Foodlist[orderchoice]
            PriceforItem = Pricelist[orderchoice]

            orderAmount = input("How many orders of this item: ")
            try:
                orderAmount = int(orderAmount)
                TableChoice.add_order(Choice, orderAmount, PriceforItem)
                main(Username, TableList)

            except:
                print("That is not an acceptable answer")
                LoadorderMenu(Username, TableList, TableChoice)

        else:
            print("That is not an acceptable answer")
            LoadorderMenu(Username, TableList, TableChoice)

    except ValueError:
        print(f"DebUgger: Error: Cannot convert '{TableChoice}' to an integer. Rerunning Fuction")
        LoadorderMenu(Username, TableList, TableChoice)

def PrepareBill(Username,TableList):
    count = 1
    tempArr = []
    for x in TableList:
        if x.waiter == Username:
            tempArr.append(x)
            print(f'{count}: Table {x.number}')
            count += 1

    if len(tempArr) == 0:
        print(f"There are no tables assigned to: {Username}")
        main(Username, TableList)

    TableChoice1 = input("Enter Table Choice: ")

    try:
        TableChoice1 = int(TableChoice1)
        TableChoice1 -= 1 

        if TableChoice1 >= 0 and TableChoice1 < len(tempArr):
            tableChosen = tempArr[TableChoice1]
            tableChosen.prepare_bill()
            main(Username, TableList)
        else:
            print('That value is not in our system')
            PrepareBill(Username,TableList)

    except ValueError:
        print(f"Debugger: Error: Cannot convert '{TableChoice1}' to an integer. Rerunning Fuction")
        PrepareBill(Username, TableList)

def CompleteSale(Username, TableList):
    count = 1
    tempArr = []
    for x in TableList:
        if x.waiter == Username:
            tempArr.append(x)
            print(f'{count}: Table {x.number}')
            count += 1

    if len(tempArr) == 0:
        print(f"There are no tables assigned to: {Username}")
        main(Username, TableList)

    TableChoice = input("Choose a table: ")

    try:
        TableChoice = int(TableChoice)
        TableChoice -= 1 
        if TableChoice >= 0 and TableChoice < len(tempArr):
            TableChosen = tempArr[TableChoice]
            TableChosen.create_bill_file()
            TableChosen.clear_waiter()
            TableChosen.clear_orders()
            main(Username, TableList)
        else:
            print('That value is not in our system')
            PrepareBill(Username,TableList)

    except ValueError:
        print(f"Debugger: Error: Cannot convert '{TableChoice}' to an integer. Rerunning Fuction")
        LoadorderMenu(Username, TableList, TableChoice)

def CashUp(Username,TableList):
    print("Generating Total of all tables. ")

    TotalCash = 0


    for x in TableList:
        TotalCash += x.Priceattained
    print(f"The Total for the day is {TotalCash}")

def main(Username, TableList):
    print("-----------------------------|")
    print("1. Assign Table \n2. Change customers \n3. Add to Order \n4. Prepare bill \n5. Complete Sale \n6. Cash up \n0. Log Out")
    print("-----------------------------|")

    choice = input("Pick an Option: ")

    try:
        choice = int(choice)

        if choice >= 0 and choice < 6:
            if choice == 0:
                print("Logging you out")
                loginMenu(TableList)

            if choice == 1:
                assignTableToWaiter(Username, TableList)

            if choice == 2:
                ChangeCustomers(Username, TableList)

            if choice == 3:
                AddOrder(Username, TableList)

            if choice == 4:
                PrepareBill(Username,TableList)

            if choice == 5:
                CompleteSale(Username, TableList)

            if choice == 6:
                CashUp(Username,TableList)
                
            else:
                print("That is not an acceptable answer")
                AddOrder(Username,TableList)

    except ValueError:
        print(f"Debugger: Error: Cannot convert '{choice}' to an integer. Rerunning Fuction")
        LoadorderMenu(Username, TableList, choice)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
table4 = Table(4)
table5 = Table(5)
table6 = Table(6)
table7 = Table(7)
TableList = [table1,table2,table3,table4,table5,table6,table7]



def Mainmain(TableList):
    Username = input("What is your user name: ")
    Password = input("What is your password: ")


    if UsernameFunction(Username, Password, TableList) == True:
        main(Username,TableList)

    else:
        Mainmain(TableList)

def loginMenu(TableList):

    print("1. Login \n2. Exit")
    x = input("Please choose an Option: ")

    if x == "1":
        print()
        Mainmain(TableList)
    elif x == "2":
        print("System Exiting")
    else:
        print("That value is not in our system. Try again")
        loginMenu(TableList)

loginMenu(TableList)



