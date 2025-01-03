# Slot_Machine

# Summary of the Game Flow
# Deposit money.
# Choose how many lines to bet on.
# Choose how much to bet per line.
# Spin the slot machine.
# Check if you won and update your balance.
# Repeat until you quit!

# Simplified Slot Machine Game

import random

# Constants for the game
MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum bet per line
MIN_BET = 1    # Minimum bet per line
ROWS = 3       # Number of rows in the slot machine
COLS = 3       # Number of columns in the slot machine

# Symbols and their properties
symbol_count = {
    "A": 2,  # Symbol A appears 2 times
    "B": 4,  # Symbol B appears 4 times
    "C": 6,  # Symbol C appears 6 times
    "D": 8   # Symbol D appears 8 times
}

symbol_value = {
    "A": 5,  # Winning multiplier for A
    "B": 4,  # Winning multiplier for B
    "C": 3,  # Winning multiplier for C
    "D": 2   # Winning multiplier for D
}

# Function 1: Ask the user for their deposit
def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            if int(amount) > 0:
                return int(amount)
            else:
                print("Please enter a valid amount greater than 0.")
        else:
            print("Please enter a valid amount greater than 0.")
    '''
    This function asks the user to input an initial deposit amount.
    - It ensures that the input is a positive integer.
    - If valid, it returns the deposit amount.
    '''

# Function 2: Ask the user for the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            if 1 <= int(lines) <= MAX_LINES:
                return int(lines)
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print(f"Please enter a number between 1 and {MAX_LINES}.")
    '''
    This function asks the user to specify the number of lines to bet on.
    - It validates that the input is a number between 1 and MAX_LINES.
    - Returns the chosen number of lines.
    '''

# Function 3: Ask the user for the bet amount per line
def get_bet():
    while True:
        amount = input(f"Enter your bet amount per line (${MIN_BET}-${MAX_BET}): $")
        if amount.isdigit():
            if MIN_BET <= int(amount) <= MAX_BET:
                return int(amount)
            else:
                print(f"Please enter a valid amount between ${MIN_BET} and ${MAX_BET}.")
        else:
            print(f"Please enter a valid amount between ${MIN_BET} and ${MAX_BET}.")
    '''
    This function prompts the user to enter the amount to bet per line.
    - Ensures the amount is between MIN_BET and MAX_BET.
    - Returns the validated bet amount.
    '''

# Function 4: Generate the slot machine's random symbols
def get_symbol_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)  # Add each symbol multiple times

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    '''
    This function generates a random layout for the slot machine.
    - Each column is filled with random symbols based on their frequency.
    - Ensures no duplicate symbols within a single column.
    - Returns the layout as a list of columns.
    '''

# Function 5: Print the slot machine's symbols
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))
    '''
    This function displays the slot machine layout.
    - Iterates through rows and prints symbols separated by " | ".
    - Makes the output easy to read.
    '''  
    
# Function 6: Check winnings
def check_winnings(columns, lines, bet, values): 
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
    '''
    This function calculates the winnings based on the slot machine result.
    - Checks each line to see if all symbols match across columns.
    - Calculates total winnings and identifies winning lines.
    - Returns the winnings and the list of winning lines.
    '''
      
# Function 7: Play one round of the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient balance. Your current balance is ${balance}, but you need ${total_bet}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}.")

    slots = get_symbol_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings > 0:
        print(f"You won ${winnings}!")
    else:
        print("No wins this time.")

    if winning_lines:
        print(f"Winning lines: {', '.join(map(str, winning_lines))}")

    return winnings - total_bet
    '''
    This function handles one round of the game.
    - Prompts the user for the number of lines and bet amount.
    - Checks if the user has enough balance to place the bet.
    - Spins the slot machine, displays the result, and calculates winnings.
    - Returns the net change in balance (winnings minus total bet).
    '''
      
# Function 8: Main game loop
def main(): 
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press Enter to play (q to quit): ")
        if answer.lower() == "q":
            break
        else:
            balance += spin(balance)
    print(f"Game over! Your final balance is ${balance}.")
    '''
    This is the main function that controls the game flow.
    - Asks the user for an initial deposit.
    - Allows the user to play multiple rounds or quit the game.
    - Updates the balance after each round and displays the final balance.
    '''
      
# Run the game
if __name__ == "__main__":
    '''
    The "if __name__ == \"__main__\":" block ensures the game runs
    only when this script is executed directly.
    It calls the main function to start the game.
    '''
    main()











