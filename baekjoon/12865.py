import sys
input=sys.stdin.readline

n, k=map(int, input().split())
knap=[[0 for _ in range(k+1)] for _ in range(n+1)]

W=[]
V=[]
for _ in range(n):
    w,v=map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1, n+1):
    for j in range(1, k+1):
        if W[i-1]>j:
            knap[i][j]=knap[i-1][j]
        else:
            knap[i][j]=max(knap[i-1][j], V[i-1]+knap[i-1][j-W[i-1]])

print(knap[n][k])