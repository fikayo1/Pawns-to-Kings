print("welcome to GT bank\n\nInsert your card") 

pin=5630
balance=20000
choice=0

pin=int(input("Enter your four digit pin\n"))

if pin==pin:

    while choice != 4:

        print("\n\n**** Menu ****")
        print("1 == balance")
        print("2 ==deposit")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice=int(input("\nEnter your option:\n"))

        if choice==1:
            print("Balance = #", balance)
        
        elif choice==2:
            dep=int(input("Enter your deposit: #"))
            balance += dep
            print("\ndeposited amount: #" ,dep)
            print("balance = #", balance)
        
        elif choice==3:
            wit=int(input("Enter the amount to withdraw: #"))
            balance -= wit
            print("\nwithdrawn amount: #" ,wit)
            print("balance = #", balance)

        elif choice==4:
            print("\n Session Ended!! Goodbye")

        else:
            print("\nInvalid Entry!!")

else:
    print("Print Incorrect!! Try again")
