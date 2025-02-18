# LATIHAN 1

n = 5
for i in range(1, n + 1):
    print(*[i] * i)


# LATIHAN 2

n = 5
for i in range(1, n + 1):
    print(*range(1, i + 1))

# LATIHAN 3

n = 5
for i in range(1, n + 1):
    print(*range(n, n - i, -1))

# LATIHAN 4

n = 5
for i in range(1, n + 1):
    print(*[i] * (n - i + 1))

# LATIHAN 5

n = 5
for i in range(n, 0, -1):
    print(*range(1, i + 1))

# LATIHAN 6

n = 5
for i in range(n, 0, -1):
    print(*range(n, n - i, -1))
