import sys
input=sys.stdin.readline

n=int(input())

arr=[]
for _ in range(n):
    a=int(input())
    arr.append(a)

dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4, 11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in arr:
    print(dp[i])