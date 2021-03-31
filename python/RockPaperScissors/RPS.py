import random

while True:
    my_answer = input("Choose: rock, paper or scissors: ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break

    if my_answer != "rock" and my_answer != "paper"  and my_answer != "scissors":
        print("Choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"The computer chose: {computer_answer}")

    if computer_answer == my_answer:
        print("You tied!")
        continue

    elif my_answer == "paper" and computer_answer == "rock":
        print("You won!")
        break

    elif my_answer == "rock" and computer_answer == "scissors":
        print("You won!")
        break

    elif my_answer == "scissors" and computer_answer == "paper":
        print("You won!")
        break
    else:
        print("You lost. Try again!")