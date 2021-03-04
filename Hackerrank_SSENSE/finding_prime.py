#given a positive integer n, return true if the number is prime and false otherwise
import math 

def isprime(n):
    if n > 1: 
        for num in range(2, int(math.sqrt(n))+1):
            if n % num <= 0:
                return False
        return True
    else:
        return True

#Time Complexity: The loop iterates from 2 to sqrt(n), so the time complexity
# is O(sqrt(n))

#TESTS
print(isprime(1)) #True
print(isprime(2)) #True
print(isprime(3)) #True
print(isprime(4)) #False
print(isprime(5)) #True
print(isprime(100)) #False
print(isprime(111)) #False
