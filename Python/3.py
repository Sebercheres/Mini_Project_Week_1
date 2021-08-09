def isPrime(x):
    for i in range (2, x//2+1):
        if x % i == 0:
            return "NO"
    return "YES"

t = int(input())
for i in range (t):
    x = int(input())
    print(isPrime(x))