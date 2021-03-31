# introduced elif statement
print("AUTO LIGHT SWITCHER 3.0")
print("----")
time = input("Is it daytime, or is it nighttime? day/night ")
print("----")
if time == "day":
    print("It is daytime.")
    print("The lights are off.")
elif time == "night":
    print("It is nighttime.")
    print("The lights are on.")
else:
    print("ERROR")
    print(f"Time must be either day or night, you wrote: {time}.")