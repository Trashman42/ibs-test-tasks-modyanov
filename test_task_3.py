def is_odd(x):
    if x % 2 and x > 50:
        return 1
    return 0


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
res = list(filter(is_odd, numbers))
print(res)
