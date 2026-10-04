import random

order =random.randint(1,20)

choice = input("Enter 1 for Burger, 2 for Pizza or 3 for Pasta:  ")

match choice:
    case "1":
        print(f"You ordered a Burger, Order number- {order}")
    case "2":
        print(f"You ordered a Pizza, Order number- {order}")
    case "3":
        print(f"You ordered a Pasta, Order number- {order}")
    case _:
        print("Please enter a valid input")