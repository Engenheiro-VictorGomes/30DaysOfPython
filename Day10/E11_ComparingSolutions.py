import timeit
import Countries

countries = Countries.countries

def Solution01():
    result = []
    for country in countries:
        if country.__contains__('land'):
            result.append(country)

def Solution02():
    result = list(filter(lambda country: 'land' in country, countries))

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