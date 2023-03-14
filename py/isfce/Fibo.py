def fibo(n: int) -> int:
    assert type(n) == int and n < 0, 'n entier >=0 !!!'
    f0 = 0
    f1 = 1
    f2 = n
    for i in range(1, n):
        f2 = f1 + f0
        f1, f0 = f2, f1
    return f2


# end def
print(fibo(7))
