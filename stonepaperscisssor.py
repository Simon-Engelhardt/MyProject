import random
def paperscissorstone(user_input):
    computer = random.randint(0,2)
    if computer == 0:
        bot = "Papier"
    elif computer == 1:
        bot = "Schere"
    elif computer == 2:
        bot = "Stein"
    if user_input == bot:
        print("Unentschieden")
    elif user_input == "Stein" and bot == "Papier":
        print("Du hast verloren, der Computer hat Papier gewählt")
    elif user_input == "Stein" and bot == "Schere":
        print("You won, bot chose Schere")
    elif user_input == "Papier" and bot == "Stein":
        print("You won, bot chose Stein")
    elif user_input == "Papier" and bot == "Stein":
        print("Du hast verloren, der Computer hat Stein gewählt")
    elif user_input == "Schere" and bot == "Stein":
        print("Du hast verloren, der Computer hat Stein gewählt")
    elif user_input == "Schere" and bot == "Papier":
        print("You won, bot chosee Papier")
    else:
        print("You typed the wrong thing")
paperscissorstone(input("Please choose Papier, Stein or Schere "))