def fatorial(a=1):
    f = 1
    for c in range(a, 0, -1):
        f *= c
    return f


n = 5
print(n, fatorial(n))
