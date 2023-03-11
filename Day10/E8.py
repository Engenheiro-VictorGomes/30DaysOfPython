# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
# 
# Solution 01:
for i in range(101):
    if i%2==0:
        print(i) 

# Solution 02:
listEvenNumber = [i for i in range(101) if i%2==0]
for number in listEvenNumber:
    print(number)