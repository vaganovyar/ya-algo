n = int(input()) + 1
sieve = [False] * n
sieve[0] = True
sieve[1] = True
for i in range(2, n):
    if not sieve[i]:
        for j in range(i * i, n, i):
            sieve[j] = True
for i in range(n):
    if not sieve[i]:
        print(i)
