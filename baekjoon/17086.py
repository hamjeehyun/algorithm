from collections import deque
import sys
input=sys.stdin.readline

def BFS(x, y):
    global visited_value
    queue=deque()
    queue.append((x, y))

    visited_value+=1
    visited[x][y]=visited_value

    length=0

    while queue:
        length+=1

        for _ in range(len(queue)):
            x, y=queue.popleft()

            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<m and visited[nx][ny]<visited_value:
                    if graph[nx][ny] == 1:
                        return length
                    else:
                        queue.append((nx, ny))
                        visited[nx][ny]=visited_value
    return length


dx=[-1, 1, 0, 0, 1, -1, -1, 1]
dy=[0, 0, -1, 1, 1, -1, 1, -1]

n, m=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]


visited=[[0]*m for _ in range(n)]
max_distance=0
visited_value=0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            max_distance=max(max_distance, BFS(i,j))

print(max_distance)