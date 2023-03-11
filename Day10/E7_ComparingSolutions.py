import timeit

def Solution01():
    list = []
    for i in range(101):
        if i%2==0:
            list.append(i)

def Solution02():
    listEvenNumber = [i for i in range(101) if i%2==0]


# 
n = 1000000
results = {}
for name, function in globals().copy().items():
    if callable(function):
        time = timeit.timeit(function, number=n)
        results[name] = time
        #print(f"{function.__name__} takes {time} to be complete {n} times.")

fastest = min(results, key=results.get)
print(f"Fastest was: {fastest}, with time of {results[fastest]}s, after repeat {n} times.")

print("Comparing to the fastest each function is slower: ")
for name, time in results.items():
    percent = ((time/results[fastest])-1)*100
    print(f"      {name} =  +{percent:.2f}%")


# Conclusion: if you want to use each number inside the list, Solution 01 is better 20%. If you need the list, Solution 02 is better 20%.