import random

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) Rock ✊")
print("2) Paper ✋")
print("3) Scissors ✌️")

play_again = "yes"

while play_again == "yes":

    player = int(input("Pick a number: "))
    computer = random.randint(1, 3)

    if player == 1 and computer == 1:
        print("You chose: ✊")
        print("CPU chose: ✊")
        print("Draw!")
    elif player == 1 and computer == 2:
        print("You chose: ✊")
        print("CPU chose: ✋")
        print("You lost!")
    elif player == 1 and computer == 3:
        print("You chose: ✊")
        print("CPU chose: ✌️")
        print("You won!!!")
    elif player == 2 and computer == 1:
        print("You chose: ✋")
        print("CPU chose: ✊")
        print("You won!!!")
    elif player == 2 and computer == 2:
        print("You chose: ✋")
        print("CPU chose: ✋")
        print("Draw!")
    elif player == 2 and computer == 3:
        print("You chose: ✋")
        print("CPU chose: ✌️")
        print("You lost!")
    elif player == 3 and computer == 1:
        print("You chose: ✌️")
        print("CPU chose: ✊")
        print("You lost!")
    elif player == 3 and computer == 2:
        print("You chose: ✌️")
        print("CPU chose: ✋")
        print("You won!!!")
    elif player == 3 and computer == 3:
        print("You chose: ✌️")
        print("CPU chose: ✌️")
        print("Draw!")
    else:
        print("Try again.")

    play_again = input("Play again? (yes/no): ").lower()

print("Thanks for playing!")
