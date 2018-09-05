import math as math

def prime(n):
    a = [1] * n
    l = int(math.sqrt(n))
    for i in range(2,l+1):
        a[2*i:-1:i] = [0] * len(a[2*i:-1:i])
    primes = []
    for i in range(len(a)):
        if a[i] == 1:
            primes.append(i)

    return primes

if __name__ == "__main__":
    print(prime(100))