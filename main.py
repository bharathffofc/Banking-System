import csv

def account_creation(n,name,password,initial_deposit):
    if initial_deposit>=100:
        with open("data.csv","a",newline='') as f:
            fieldnames = ['Account Number', 'Name', 'Password', 'Initial Deposit']
            write = csv.DictWriter(f, fieldnames=fieldnames)
            write.writerow({'Account Number':n, 'Name':name, 'Password':password, 'Initial Deposit':initial_deposit})
    else:
        print("Insufficient deposit amount...")

if __name__ == '__main__':
    acc_num=1
    with open("data.csv","w",newline='') as f:
        f.write("Account Number,Name,Password,Initial Deposit\n")
    while True:
        print("Enter Your Choice: ")
        print("1 for Account Creation.")
        print("0 for Exit.")
        choice=int(input())
        match choice:
            case 1:
                name=input("Enter Your name: ")
                password=input("Enter a password for Login: ")
                initial_deposit=int(input("Enter the Initial Deposit Amount: "))
                account_creation(acc_num,name,password,initial_deposit)
                acc_num+=1

            case 0:
                print("Exit the Program...")
                break