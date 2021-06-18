import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u, v = map(int, input().split())
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)

def dfs(x):
    visited[x] = True
    
    for i in arr[x]:
        if visited[i] == False:
            dfs(i)

ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)