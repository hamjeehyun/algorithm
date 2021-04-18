from sys import stdin
MAX_SIZE=100001


t = int(stdin.readline())
dp = [1] * MAX_SIZE

for i in range(2, MAX_SIZE):
    dp[i] += dp[i - 2]

for i in range(3, MAX_SIZE):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(stdin.readline())
    print(dp[n])