# Normally, while solving challenge exercises, I find better ways to solve the same problem,
# and therefore new solutions emerge. 
# These solutions are usually better because they are easier to read/understand and have better performance.

# But in today's Exercise 2, I came across something different.
# I found the first solution easier to understand than the second,
# so I decided to try to make the code easier to read, resulting in Solution 3.

# As I didn't want to lose performance, I made this script to see if there would be any loss,
# and how much it would be.


import timeit

def solution01():
    Countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    Countries2 = ['China', 'Russia', 'USA', 'Sweden', 'Norway', 'Denmark']
    list1 = []
    list2 = []
    for i, Country in enumerate(Countries1):
        if i < len(Countries1)/2:
            list1.append(Country)
        else:
            list2.append(Country)
    result1 = list1,list2
    list1 = []
    list2 = []
    for i, Country in enumerate(Countries2):
        if i < len(Countries2)/2:
            list1.append(Country)
        else:
            list2.append(Country)
    result2 = list1,list2

def solution02():
    Countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    Countries2 = ['China', 'Russia', 'USA', 'Sweden', 'Norway', 'Denmark']
    result1 = Countries1[:int((len(Countries1)+1)/2)],Countries1[int((len(Countries1)+1)/2):]
    result2 = Countries2[:int((len(Countries2)+1)/2)],Countries2[int((len(Countries2)+1)/2):]

def solution03():
    Countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    Countries2 = ['China', 'Russia', 'USA', 'Sweden', 'Norway', 'Denmark']
    middlePos = int((len(Countries1)+1)/2)
    result1 = Countries1[:middlePos],Countries1[middlePos:]
    middlePos = int((len(Countries2)+1)/2)
    result2 = Countries2[:middlePos],Countries2[middlePos:]

# 
n = 1000000
results = {}
for name, function in globals().copy().items():
    if callable(function):
        time = timeit.timeit(function, number=n)
        results[name] = time
        #print(f"{function.__name__} takes {time} to be complete {n} times.")

fastest = min(results, key=results.get)
print(f"Fastest was: {fastest}, with time of {results[fastest]}")

print("% diff")
for name, time in results.items():
    percent = ((time/results[fastest])-1)*100
    print(f"{name} =  +{percent:.2f}%")
