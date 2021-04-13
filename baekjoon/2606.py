import sys
input=sys.stdin.readline

def DFS(graph, start, visited):
    global cnt
    visited[start]=True
    cnt+=1

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)  


n = int(input())
k = int(input())
visited=[False for _ in range(n+1)]
cnt=0

graph=[[] for _ in range(n+1)]
graph[0]=[0,0]

for _ in range(k):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

DFS(graph, 1, visited)

print(cnt-1)