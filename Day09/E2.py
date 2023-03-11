# 2.0 Write a code which gives grade to students according to theirs scores:
#     80-100, A
#     70-89, B
#     60-69, C
#     50-59, D
#     0-49, F 

def getScore(score):
    if score < 0 or score > 100:
        raise ValueError
    if score > 80:
        return 'A'
    elif score > 70:
        return 'B'
    elif score > 60:
        return 'C'
    elif score > 50:
        return 'D'
    else:
        return 'F'

try:
    getScore(-1)
    assert False, "getScore() fail with negative value"
except ValueError:
    pass

try:
    getScore(101)
    assert False, "getScore() fail with value higher than 100"
except ValueError:
    pass

assert getScore(100) == 'A', "Fail for 100"
assert getScore(90) == 'A', "Fail for 90"
assert getScore(80) == 'B', "Fail for 80"
assert getScore(70) == 'C', "Fail for 70"
assert getScore(60) == 'D', "Fail for 60"
assert getScore(50) == 'F', "Fail for 50"
assert getScore(0) == 'F', "Fail for 0"

print("getScore() works")

# 2.1 Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer

def getSeason(month):
    autumnMonths = ['September', 'October', 'November']
    winterMonths = ['December', 'January', 'February']
    springMonths = ['March', 'April', 'May']
    summerMonths = ['June', 'July', 'August']
    if month in (autumnMonths + winterMonths + springMonths + summerMonths):
        if month in autumnMonths:
            return 'Autumn'
        elif month in winterMonths:
            return 'Winter'
        elif month in springMonths:
            return 'Spring'
        elif month in summerMonths:
            return 'Summer'
    else:
        raise ValueError

# userMonth = input("Enter the month: ")
# print(getSeason(userMonth))
assert getSeason('September') == 'Autumn', 'Fail for September'
assert getSeason('October') == 'Autumn', 'Fail for October'
assert getSeason('November') == 'Autumn', 'Fail for November'
assert getSeason('December') == 'Winter', 'Fail for December'
assert getSeason('January') == 'Winter', 'Fail for January'
assert getSeason('February') == 'Winter', 'Fail for February'
assert getSeason('March') == 'Spring', 'Fail for March'
assert getSeason('April') == 'Spring', 'Fail for April'
assert getSeason('May') == 'Spring', 'Fail for May'
assert getSeason('June') == 'Summer', 'Fail for June'
assert getSeason('July') == 'Summer', 'Fail for July'
assert getSeason('August') == 'Summer', 'Fail for August'
print("getSeason() works")

# 2.2 The following list contains some fruits: 
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
newFruit = input('Enter your fruit: ')
if newFruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(newFruit)
    print(fruits)