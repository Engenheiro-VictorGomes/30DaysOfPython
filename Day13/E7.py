# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

# y = ax+b
# y-intecept = when y=0
#   0 = ax+b
#   x = -b/a
yIntercept = lambda a,b : -b/a

dictToTest = { (1,-1): 1,
               (1,1): -1,
               (-1,1): 1,
               (-1,-1): -1,
               (2,-1): 0.5,
               (2,1): -0.5,
               (-2,1): 0.5,
               (-2,-1): -0.5,
               (1,-2): 2,
               (1,2): -2,
               (-1,2): 2,
               (-1,-2): -2
            }

for key,value in dictToTest.items():
    assert yIntercept(key[0],key[1]) == value, f'Fail for {key}'    
print("yIntercept() works")
