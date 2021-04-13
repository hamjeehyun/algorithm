from collections import deque
import sys
input=sys.stdin.readline

def BFS(x, y):
    queue=deque()
    queue.append((x, y))
    graph[x][y]=0
    
    cnt=1

    while queue:
        x, y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            if graph[nx][ny] != 0:
                queue.append((nx, ny))
                graph[nx][ny]=0
                cnt+=1
    return cnt

n, m, k = map(int, input().split())
graph=[[0]*m for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1]=1


size = -1
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            size = max(size, BFS(i, j))

print(size)