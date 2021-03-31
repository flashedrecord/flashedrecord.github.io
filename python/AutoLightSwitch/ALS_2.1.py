# added user input
print("AUTO LIGHT SWITCHER 2.1")
print("----")
time = input("Is it daytime, or is it nighttime?")
print("----")

if time == "day":
    print("It is daytime.")
    print("The lights are off.")

if time == "night":
    print("It is nighttime.")
    print("The lights are on.")

if time != "day" or "night":
    print("ERROR")
    print("Time has to be either day or night.")