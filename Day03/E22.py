# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#    Enter number of years you have lived: 100
#    You have lived for 3153600000 seconds.

# no Magic numbers
daysInYear = 365
hoursInDay = 24
minutesInHour = 60
secondInMinutes = 60
maxYearsLive = 100


years = float(input("Enter number of years you have lived: "))
print(f"You can live for {int(maxYearsLive*daysInYear*hoursInDay*minutesInHour*secondInMinutes)} seconds.")
print(f"You have lived for {int(years*daysInYear*hoursInDay*minutesInHour*secondInMinutes)} seconds.")
diff = int(years*daysInYear*hoursInDay*minutesInHour*secondInMinutes - maxYearsLive*daysInYear*hoursInDay*minutesInHour*secondInMinutes)
print(f"You can live more {diff} seconds.")
