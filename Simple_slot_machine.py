import random
fruit = ["🍒", "🍋", "🍉", "🍌", "🫐", "🍐", "7", "🥝", "🍓", "🍍"]

while True:
    amount = input("Enter your starting balance (press n to exit): ").strip().lower()
    if amount == "n":
        break
    try:
        balance = int(amount)
        if balance <= 0:
            print("Please enter a positive number")
        else:
            print("Welcome to the Slot Machine Game!")
            print(f"You start with ${balance}")
            print("----------------------------------")
            print(f"Current balance: ${balance}")
            while True:
                if balance <= 0:
                    print("You ran out of money")
                    break
                bet_money = input(f"Enter your bet amount: ")
                try:
                    bet_amount = int(bet_money)
                    if bet_amount <= 0 or bet_amount > balance:
                        print(f"Invalid bet amount. You can bet between 1 and {balance}")
                    else:
                        balance = balance - bet_amount
                        print(f"Your current balance is ${balance}")
                        x = random.choice(fruit)
                        y = random.choice(fruit)
                        z = random.choice(fruit)
                        print(f" {x} | {y} | {z} ")

                        if x == y == z == fruit[6]:
                            print(f"JACKPOT WIN!!!! YOU WIN {bet_amount * 7}")
                            balance += bet_amount * 7
                        elif x == y == z:
                            print(f"You won {bet_amount * 3}")
                            balance += bet_amount * 3
                        elif x == y or x == z or y == z:
                            print(f"You won {bet_amount * 2}")
                            balance += bet_amount * 2
                        else:
                            print("You lost!")
                            
                        print(f"Your current balance is ${balance}")
                        user_choice = input("Do you want to continue? (y/n): ").lower()
                        if user_choice == "y":
                            continue
                        elif user_choice == "n":
                            break
                        else:
                            print("Invalid input. Please enter y or n")
                except ValueError:
                    print(f"Invalid bet amount. You can bet between 1 and {balance}")
    except ValueError:
        print("Please enter a valid starting balance")






