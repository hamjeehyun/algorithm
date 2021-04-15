from collections import deque
import sys
input=sys.stdin.readline
MAX_SIZE=100001

n, k = map(int, input().split())

check=[-1]*MAX_SIZE
check[n]=0

path=[-1]*MAX_SIZE

queue=deque()
queue.append(n)

while queue:
    now = queue.popleft()

    if now == k:
        print(check[k])
        p=[]
        while now!= n:
            p.append(now)
            now=path[now]
        p.append(n)
        p.reverse()
        print(' '.join(map(str, p))) 
        break

    for next_ in [now*2, now+1, now-1]:
        if 0 <= next_ < MAX_SIZE:
            if check[next_] == -1 or check[next_] >= check[now] + 1:
                queue.append(next_)
                path[next_]=now
                check[next_] = check[now] + 1