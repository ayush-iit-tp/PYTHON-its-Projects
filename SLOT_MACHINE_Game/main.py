# Slot_Machine
import random
# Announcing Global Constant
Max_Lines = 3
Max_Bet = 1000
Min_Bet = 1
# No of rows and columns in slot machine are defined here:
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
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
    lines = 0
    while True:
        lines = input("How much number of lines to bet on between (1-" +str(Max_Lines)+")? ")
        '''
        str(Max_Lines) converts the value of Max_Lines to a string.
        ")? " is another string literal.
        '''
        if lines.isdigit():
            lines =int(lines)
            if 1 <=lines <= Max_Lines:
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
# Generate Outcome of the slot machine
def get_symbol_spin(rows, cols, symbols):
    all_symbols = []
    '''
    Main question is how to select random symbol?
    '''
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for col in range(cols): # we have 3 columns so for doing everything 3 times , we are using this for loop
        column =[]
        current_symbols = all_symbols[:] # it creates a copy of all symbols but by making changes in current_symbols,  all_symbols will not be affected
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
            # removing the value so that we  will not pick it again
        columns.append(column) # adding that value to the column
    return columns
# printing values on the slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])): # means no of elements in each column
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print()
# Final function to check winnings means all symbols are same in a row or not
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
#
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You don't have enough money to bet that amount, your total balance is ${balance}. \nYou need ${total_bet} in your balance amount.\nAdd ${total_bet - balance} to your total balance.\nHave a nice day!")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.Total bet is ${total_bet}.\nKeep Playing!")

    slots = get_symbol_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You win! Your total balance is ${balance}.")
    print(f"You have won on", *winning_lines)
    return winnings - total_bet
# Our main Function
def main():
    balance = deposit()
    while True:
        print(f"CURRENT BALANCE: ${balance}")
        answer =input("Press Enter to Play! (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"Your CURRENT BALANCE is: ${balance}")
main()










