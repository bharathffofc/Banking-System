import csv

flag=False  #for storing the boolean value to give access for banking operation

def account_creation(n,name,password,initial_deposit):  #function for account creation
    if initial_deposit>=100: #check if the initial deposit is greater than 100
        with open("data.csv","a",newline='') as f:    #open the file in append mode to append data to the csv file
            fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit']
            write = csv.DictWriter(f, fieldnames=fieldnames)
            write.writerow({'Account Number':n, 'Name':name, 'Password':password, 'Initial Deposit':initial_deposit}) #write data to csv file using writerow operation
            print("Account Created Successfully.")
            with open("statement.csv","a",newline='') as file:
                file.write(f"{n},Account Creation,{initial_deposit}\n")  #append the data to account statement csv file
    else:
        print("Insufficient deposit amount...")

def login(n,password):
    global flag #initially flag will be false
    with open("data.csv","r",newline='') as f:
        res=csv.DictReader(f) #store csv file in a dictionary
        for r in res:
            if int(r["Account Number"])==n and r["Password"]==password: #check if the account number and password matches,if matches give access
                flag = True  #make flag as true if condition satisfies
                break
        if flag:
            return "Login Successful."
        else:
            return "Login Failed..."

def balance(n):
    with open("data.csv","r",newline='') as f: #open file in read mode and store it in a dictionary
        res=csv.DictReader(f)
        for r in res:
            if n==int(r["Account Number"]):  #check if acc no matches,if matches show balance
                with open("statement.csv", "a", newline='') as file:
                    file.write(f"{n},Balance,{int(r["Initial Deposit"])}\n")    #append the data to account statement csv file
                return f"Balance: {int(r["Initial Deposit"])}"
        return "Wrong Account Number..."

def deposit(n,deposit_amount):
    df = False
    with open("data.csv","r",newline='') as f: #open file in read mode and store it in a list of dictionary
        res=list(csv.DictReader(f))
        for r in res:
            if n==int(r["Account Number"]): #if account number matches,perform deposit operation
                df=True #deposit flag for writing data to csv file
                r["Initial Deposit"]=str(int(r["Initial Deposit"])+deposit_amount)#increment balance by deposit amount
                with open("statement.csv", "a", newline='') as file:
                    file.write(f"{n},Deposit,{deposit_amount}\n")  #append the data to account statement csv file
        if df:
            with open("data.csv","w",newline='') as f:
                fieldnames=['Account Number', 'Name', 'Password', 'Initial Deposit'] #open file in write mode and write all the data back into it
                write=csv.DictWriter(f,fieldnames=fieldnames)
                write.writeheader()
                write.writerows(res)
            return "Deposit Successful."
        else:
            return "Invalid Account Number"

def withdraw(n,withdraw_amount,):
        wf = False
        with open("data.csv","r",newline='') as f:
            res=list(csv.DictReader(f))
            for r in res:
                if int(r["Account Number"])==n and int(r["Initial Deposit"])>withdraw_amount+100: #check if acc  no matches and balance is greater than withdraw
                    wf=True #withdrwa flag for writing data
                    r["Initial Deposit"]=str(int(r["Initial Deposit"])-withdraw_amount) #withdraw operation
                    with open("statement.csv", "a", newline='') as file: #append the data to account statement csv file
                        file.write(f"{n},Withdraw,{withdraw_amount}\n")

            if wf:
                with open("data.csv","w",newline='') as f:
                    fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit'] #to write the data back into file using dictwriter
                    write=csv.DictWriter(f,fieldnames=fieldnames)
                    write.writeheader()
                    write.writerows(res)
                return "Withdraw Successful."
            else:
                return "Withdraw amount is greater than balance... or Wrong Account Number"

def transfer(n1,n2,amount):
    sf = False #sender flag
    rf = False  #receiver flag
    if amount>0:    #check if the sending amount is valid
        with open("data.csv","r",newline='') as f:
            res=list(csv.DictReader(f))
            for r in res:
                if n1==int(r["Account Number"]) and int(r["Initial Deposit"])>amount+100: #check if sender acc_no matches and sending amount is greater than the min bal plus 100
                    sf=True
                    r["Initial Deposit"]=str(int(r["Initial Deposit"])-amount) #decrement amount for sender
            if sf:
                for r in res:
                    if n2==int(r["Account Number"]): #check if receiver acc_no matches
                        rf=True
                        r["Initial Deposit"]=str(int(r["Initial Deposit"])+amount) #increment balance of receiver
                        with open("statement.csv", "a", newline='') as file:
                            file.write(f"{n1},Transfer from {n1} to {n2},{amount}\n")   #append the data to account statement csv file
                if rf:
                    with open("data.csv","w",newline='') as f:  #to write the data back into file using dictwriter
                        fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit']
                        write = csv.DictWriter(f,fieldnames=fieldnames)
                        write.writeheader()
                        write.writerows(res)
                    return f"Amount {amount} is debited from {n1} and credited to {n2}"
                else:
                    return "Invalid Account Number"
            else:
                return "Sending amount is Greater than balance ot invalid Account Number"
    else:
        print("Invalid Amount,Amount Should be Greater than 0")

def statement(n):
    with open("statement.csv","r",newline='') as file: #open file in read mode and store it in a list
        res=list(csv.DictReader(file))
        ans=[]
        for r in res:
            if int(r["Account Number"])==n: #check if acc_no matches,if matches print the acc_statement
                ans.append(f"{r["Account Number"]},{r["Operation"]},{r["Amount"]}")
        return ans
if __name__ == '__main__':
    acc_num=1
    with open("data.csv","w",newline='') as f: #initially write the column headers by opening file in write mode
        f.write("Account Number,Name,Password,Initial Deposit\n")
    with open("statement.csv", "w", newline='') as file:
        file.write("Account Number,Operation,Amount\n")
    while True:
        print("Enter Your Choice: ")
        print("1 for Account Creation.")
        print("2 for Login.")
        print("0 for Exit.")
        choice=int(input())
        match choice:
            case 1: #case to handle account creation
                name=input("Enter Your name: ")
                password=input("Enter a password for Login: ")
                initial_deposit=int(input("Enter the Initial Deposit Amount: "))
                account_creation(acc_num,name,password,initial_deposit)
                acc_num+=1

            case 2:#case to handle to login
                acc_num=int(input("Enter Account number: "))
                password=input("Enter the Password: ")
                msg=login(acc_num,password)
                if msg:
                    print("Login Successful")
                    while True:
                        print("\n1 for Check Balance.")
                        print("2 for Deposit.")
                        print("3 for Withdraw.")
                        print("4 for Transfer.")
                        print("5 for Bank statement.")
                        print("6 for Logging Out.\n")
                        choice=int(input())
                        match choice:
                            case 1: #case for balance
                                m=balance(acc_num)
                                print(m)

                            case 2: #case for deposit
                                deposit_amount=int(input("Enter the amount to deposit: "))
                                m=deposit(acc_num,deposit_amount)
                                print(m)

                            case 3: #case for withdraw
                                withdraw_amount=int(input("Enter the Withdraw amount: "))
                                m=withdraw(acc_num,withdraw_amount)
                                print(m)

                            case 4: #case for transfer
                                acc_n2=int(input("Enter the Account Number of the Receiver: "))
                                amount=int(input("Enter the Amount to Send: "))
                                m=transfer(acc_num,acc_n2,amount)
                                print(m)

                            case 5:
                                res=statement(acc_num)
                                print("Bank Statement: \n")
                                for r in res:
                                    print(r)

                            case 6:
                                print("Logging Out...")
                                break
                else:
                    print("Login Failed...")
                    print("Account number or password is invalid")

            case 0: #case for exit
                print("Exit the Program...")
                break

















