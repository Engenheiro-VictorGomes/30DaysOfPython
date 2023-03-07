# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#    Enter hours: 40
#    Enter rate per hour: 28
#    Your weekly earning is 1120

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {int(hours * rate)}")