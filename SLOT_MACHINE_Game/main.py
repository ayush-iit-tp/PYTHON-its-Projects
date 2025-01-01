# Slot_Machine
import random
# Announcing Global Constant
Max_Lines = 3
Max_Bet = 10000
Min_Bet = 1

ROWS = 3
COLS = 3


# To take amount from the user on which he will do betting
def deposit():
    while True:
        amount = input("How much do you want to deposit?: $")
        if amount.isdigit():
            amount =int(amount)
            if   amount >0 :
                break
            else:
                print("Amount must be greater than 0")
                '''
                if amount.isdigit(): Take only if amount entered is number and then We need the amount to be converted into integer from string.
                '''
        else:
            print("Please Enter a number.")
            '''
            else if you are not all entering a number do this
            '''
    return amount
# To take number of lines from the user on which he will do betting
def get_number_of_lines():
    while True:
        lines = input("How much number of lines to bet on between (1-" +str(Max_Lines)+")? ")
        '''
        str(Max_Lines) converts the value of Max_Lines to a string.
        ")? " is another string literal.
        '''
        if lines.isdigit():
            lines =int(lines)
            if 1 <=lines <= 3:
                break
            else:
                print("Lines must be entered as a positive number")
                '''
                if lines.isdigit(): Take only if no of lines entered are number and then We need the no of lines to be converted into integer from string.
                '''
        else:
            print("Please Enter a number.")
            '''
            else if you are not all entering a number do this
            '''
    return lines
# To take amount from the user on which he will do betting on each line
def get_bet():
    while True:
        amount = input("How much do you want to bet on each line?: $")
        if amount.isdigit():
            amount =int(amount)
            if  Min_Bet <= amount <= Max_Bet :
                break
            else:
                print(f"Amount must be a between ${Min_Bet} and ${Max_Bet}")
                '''
                if amount.isdigit(): Take only if amount entered is number and then We need the amount to be converted into integer from string.
                '''
        else:
            print("Please Enter a number.")
            '''
            else if you are not all entering a number do this
            '''
    return amount
# Our main Function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money to bet that amount, your total balance is ${balance}. \nYou need ${total_bet} in your balance amount.\nAdd ${total_bet - balance} to your total balance.\nHave a nice day!")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.Total bet is ${total_bet}.\nKeep Playing!")

main()










