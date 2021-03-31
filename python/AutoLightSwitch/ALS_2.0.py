# added "if"
time = "day"
print("AUTO LIGHT SWITCHER 2.0")
print("----")

if time == "day":
    print("It is daytime.")
    print("The lights are off.")

if time == "night":
    print("It is nighttime.")
    print("The lights are on.")

if time != "day" and "night":
    print("ERROR")
    print("Time has to be either day or night.")