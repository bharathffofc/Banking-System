import csv

flag=False

def account_creation(n,name,password,initial_deposit):
    if initial_deposit>=100:
        with open("data.csv","a",newline='') as f:
            fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit']
            write = csv.DictWriter(f, fieldnames=fieldnames)
            write.writerow({'Account Number':n, 'Name':name, 'Password':password, 'Initial Deposit':initial_deposit})
    else:
        print("Insufficient deposit amount...")

def login(n,password):
    global flag
    with open("data.csv","r",newline='') as f:
        res=csv.DictReader(f)
        for r in res:
            if int(r["Account Number"])==n and r["Password"]==password:
                flag = True
                break
        if flag:
            return "Login Successful."
        else:
            return "Login Failed..."

def balance(n):
    with open("data.csv","r",newline='') as f:
        res=csv.DictReader(f)
        for r in res:
            if n==int(r["Account Number"]):
                return f"Balance: {int(r["Initial Deposit"])}"
        return "Wrong Account Number..."

def deposit(n,deposit_amount):
    df = False
    with open("data.csv","r",newline='') as f:
        res=list(csv.DictReader(f))
        for r in res:
            if n==int(r["Account Number"]):
                df=True
                r["Initial Deposit"]=str(int(r["Initial Deposit"])+deposit_amount)
        if df:
            with open("data.csv","w",newline='') as f:
                fieldnames=['Account Number', 'Name', 'Password', 'Initial Deposit']
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
                if int(r["Account Number"])==n and int(r["Initial Deposit"])>withdraw_amount+100:
                    wf=True
                    r["Initial Deposit"]=str(int(r["Initial Deposit"])-withdraw_amount)

            if wf:
                with open("data.csv","w",newline='') as f:
                    fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit']
                    write=csv.DictWriter(f,fieldnames=fieldnames)
                    write.writeheader()
                    write.writerows(res)
                return "Withdraw Successful."
            else:
                return "Withdraw amount is greater than balance... or Wrong Account Number"

def transfer(n1,n2,amount):
    sf = False
    rf = False
    with open("data.csv","r",newline='') as f:
        res=list(csv.DictReader(f))
        for r in res:
            if n1==int(r["Account Number"]) and int(r["Initial Deposit"])>amount+100:
                sf=True
                r["Initial Deposit"]=str(int(r["Initial Deposit"])-amount)
        if sf:
            for r in res:
                if n2==int(r["Account Number"]):
                    rf=True
                    r["Initial Deposit"]=str(int(r["Initial Deposit"])+amount)
            if rf:
                with open("data.csv","w",newline='') as f:
                    fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit']
                    write = csv.DictWriter(f,fieldnames=fieldnames)
                    write.writeheader()
                    write.writerows(res)
                return f"Amount {amount} is debited from {n1} and credited to {n2}"
            else:
                return "Invalid Account Number"
        else:
            return "Sending amount is Greater than balance ot invalid Account Number"

if __name__ == '__main__':
    acc_num=1
    with open("data.csv","w",newline='') as f:
        f.write("Account Number,Name,Password,Initial Deposit\n")
    while True:
        print("Enter Your Choice: ")
        print("1 for Account Creation.")
        print("2 for Login.")
        print("0 for Exit.")
        choice=int(input())
        match choice:
            case 1:
                name=input("Enter Your name: ")
                password=input("Enter a password for Login: ")
                initial_deposit=int(input("Enter the Initial Deposit Amount: "))
                account_creation(acc_num,name,password,initial_deposit)
                acc_num+=1

            case 2:
                acc_num=int(input("Enter Account number: "))
                password=input("Enter the Password: ")
                msg=login(acc_num,password)
                if msg:
                    print("Login Successful")
                    while True:
                        print("1 for Check Balance.")
                        print("2 for Deposit.")
                        print("3 for Withdraw.")
                        print("4 for Transfer.")
                        print("5 for Logging Out.")
                        choice=int(input())
                        match choice:
                            case 1:
                                m=balance(acc_num)
                                print(m)

                            case 2:
                                deposit_amount=int(input("Enter the amount to deposit: "))
                                m=deposit(acc_num,deposit_amount)
                                print(m)

                            case 3:
                                withdraw_amount=int(input("Enter the Withdraw amount: "))
                                m=withdraw(acc_num,withdraw_amount)
                                print(m)

                            case 4:
                                acc_n2=int(input("Enter the Account Number of the Receiver: "))
                                amount=int(input("Enter the Amount to Send: "))
                                m=transfer(acc_num,acc_n2,amount)
                                print(m)

                            case 5:
                                print("Logging Out...")
                                break
                else:
                    print("Login Failed...")

            case 0:
                print("Exit the Program...")
                break