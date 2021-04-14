from collections import deque
import sys
input=sys.stdin.readline

def BFS(n):
    global result
    queue=deque()
    queue.append((0, n))

    while queue:
        cnt, now=queue.popleft()

        if now==m:
            result=cnt+1
            return result

        if now*2 <= m:
            queue.append((cnt+1, now*2))
        if int(str(now)+'1') <= m:
            queue.append((cnt+1, int(str(now)+'1')))
            


n, m=map(int, input().split())
result=-1
BFS(n)
print(result)