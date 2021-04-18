import sys
input=sys.stdin.readline

n=int(input())
arr=list(input().strip())
dp=[0]*n
BOJ=['B', 'O', 'J']*(2)
print(BOJ)

i=0
for c in ['B', 'O', 'J','B', 'O']:
    while i<=n:
        if arr[i]==c:
            dp[i]=1
            break
        i+=1
        
print(dp)
result=0
cnt=1
for i in range(1, n):
    if dp[i]==1:
        result+=cnt**2
        cnt=1
    else:
        cnt+=1

if result==0: print(-1)
else: print(result)