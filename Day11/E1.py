# 1. Write a function called is_prime, which checks if a number is prime.

def is_prime(number):
    if number <= 3:
        return True
    else:
        for i in range(2,number):
            if number%i==0:
                return False
        return True

assert is_prime(1) == True, 'Fail for 1'
assert is_prime(2) == True, 'Fail for 2'
assert is_prime(3) == True, 'Fail for 3'
assert is_prime(4) == False, 'Fail for 4'
assert is_prime(5) == True, 'Fail for 5'
assert is_prime(6) == False, 'Fail for 6'
assert is_prime(7) == True, 'Fail for 7'
assert is_prime(8) == False, 'Fail for 8'
assert is_prime(9) == False, 'Fail for 9'
assert is_prime(10) == False, 'Fail for 10'
assert is_prime(11) == True, 'Fail for 11'
print("is_prime() works")