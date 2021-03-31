user_answer = input("Choose a number ")

while True:
    if user_answer.isnumeric() == True:
        user_answer = int(user_answer)
    else:
        print("Only choose a number! ")
        break

    if user_answer % 2 == 0:
        num = "even" 
    elif user_answer % 2 == 1:
        num = "odd"

    print(f"{user_answer} is {num}")

    break





