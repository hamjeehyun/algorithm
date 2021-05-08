import sys
input=sys.stdin.readline
MAX=1000000

check=[0] * (MAX+1)
check[0] = check[1] = True

for i in range(1, MAX+1):
    if not check[i]:
        j=i+i
        while j <= MAX:
            check[j] = True
            j += i

a, b = map(int, input().split())

for i in range(a, b+1):
    if not check[i]:
        print(i)