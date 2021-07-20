n = int(input())
D = [0 for _ in range(n+1)]

if n == 1: print(n)
elif n==2: print(n+1)
else:
    D[1] = 1
    D[2] = 3

    for i in range(3, n+1):
        D[i] = D[i-1] + D[i-2] * 2
    
    print(D[n]%10007)