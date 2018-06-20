import random
def paperscissorstone(user_input):
    computer = random.randint(0,2)
    if computer == 0:
        bot = "paper"
    elif computer == 1:
        bot = "scissor"
    elif computer == 2:
        bot = "stone"
    if user_input == bot:
        print("tie")
    elif user_input == "stone" and bot == "paper":
        print("You lost, the computer chose 'paper' ")
    elif user_input == "stone" and bot == "scissor":
        print("You won, the computer chose 'scissor'")
    elif user_input == "paper" and bot == "stone":
        print("You won, the computer chose stone")
    elif user_input == "paper" and bot == "stone":
        print("You lost, the computer chose stone gewählt")
    elif user_input == "scissor" and bot == "stone":
        print("You lost, the computer chose stone gewählt")
    elif user_input == "scissor" and bot == "paper":
        print("You won, the computer chose 'paper'")
    else:
        print("You typed the wrong thing")
while True:
    paperscissorstone(input("Please choose paper, stone or scissor "))
