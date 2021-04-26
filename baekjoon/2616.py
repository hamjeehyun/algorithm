import sys
input=sys.stdin.readline



N=int(input())
arr=list(map(int, input().split()))
K=int(input())

dp=[[0 for _ in range(N+1)] for _ in range(4)]
S=[0 for _ in range(N)]

S[0]=arr[0]
for i in range(1, N):
    S[i]=S[i-1]+arr[i]

print(S)
result=0
for n in range(4):
    for m in range(N):
        if n==1:
            dp[n][m] = max(dp[n][m-1], S[m] - S[m - K])
        else:
            dp[n][m] = max(dp[n][m-1], dp[n - 1][m - K] + S[m]-S[m-K])
        result=max(result, dp[n][m])

print(dp)
print(result)