import sys
input=sys.stdin.readline

n=int(input())
T=[]
P=[]
for _ in range(n):
    a, b=map(int, input().split())
    T.append(a)
    P.append(b)

d=[0]*(n+1)

for i in range(n):
    if T[i] <= n-i:
        d[i+T[i]] = max(d[i+T[i]], d[i]+P[i])
    d[i+1]=max(d[i+1], d[i])

print(d[n]) 