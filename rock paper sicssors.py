import random

options =["rock","paper","scissors"]

running= True

while running:
    player=None
    computer= random.choice(options)

    while player not in options:
        player = input("enter a choice ( rock, paper, scissors): ")

        print(f"player: {player}")
        print(f"computer: {computer}")

        if player == computer:
            print("its a tie")

        elif player =="rock" and computer =="scissors":
            print("you win!")

        elif player == "paper" and computer == "rock":
            print("you win")

        elif player == "scissors" and computer =="paper":
            print("you win")

        else:
            print("you lose")    

    xy =input("do u want to play again(y or n)").lower()
    if xy == "y":
        continue
        
    else:
        running = False
          
print("thanks for playing")            