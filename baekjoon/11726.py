n = int(input())
D = [0 for _ in range(n+1)]

if n < 3: print(n)
else:
    D[1] = 1
    D[2] = 2

    for i in range(3, n+1):
        D[i] = D[i-1] + D[i-2]

    print(D[n]%10007)