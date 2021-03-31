print("Rock Paper Scissors")
user_answer = input("Choose: rock, paper or scissors! ")

if user_answer == "rock":
    computer_answer = "paper"

elif user_answer == "paper":
    computer_answer = "scissors"
elif user_answer == "scissors":
    computer_answer = "rock"
else:
    computer_answer = f"something that beats {user_answer}"


print (f"You chose {user_answer}.")
print (f"The computer chose {computer_answer}.")
print ("You lost. Try again!")