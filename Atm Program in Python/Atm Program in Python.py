balance = 0
withdraw = 0
option = 0
deposite = 0
import sys
 
print("Welcome to the ATM")
input("Press ENTER to continue")
 
 
def another():
    answer = input("Would you like to make another transaction y/n?: ").lower()
    if answer == 'y':
        active = True
    else:
        active = False
        sys.exit("Thank you for using JTM")
 
 
active = True
 
while active:
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Balance")
    print("4: Quit")
 
    option = int(input("What would you like to do: "))
 
    if option == 1:
        deposite = int(input("How much would you like to deposit: "))
        print("Your deposited $" + str(deposite))
        balance = balance + deposite
    elif option == 2:
        print("Your total amount available for withdrawal is: $" + str(balance))
        while True:
            withdraw = int(input("Withdraw: $"))
            if withdraw > balance:
                print("Cannot withdraw more than available balance")
                continue
            balance = balance - withdraw
            break
    elif option == 3:
        print("balance: $" + str(balance))
    elif option == 4:
        sys.exit("Thanks")
