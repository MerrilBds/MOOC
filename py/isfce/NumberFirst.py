import math


def estPremier(n: int) -> bool:
    # Check if the number is greater than 2 and even
    # If it is, then it's not a prime number
    if n > 2 and n % 2 == 0:
        premier = False
    else:
        premier = True

    # Check if any odd number between 3 and the square root of n
    # can divide n evenly. If it can, then n is not a prime number.
    d = 3
    valp = d * d <= n

    while premier and valp:
        premier = n % d != 0
        d = d + 2
        valp = d * d <= n

    return premier

print(estPremier(37))
print(estPremier(3))
print(estPremier(29))










