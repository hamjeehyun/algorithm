from collections import deque
import sys
input=sys.stdin.readline
MAX_SIZE=100001

n,k=map(int, input().split())

cnt=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
check=[-1]*MAX_SIZE
check[n]=0

queue=deque()
queue.append(n)

while queue:
    now=queue.popleft()

    if now==k:
        cnt+=1

    for next_ in [now*2, now+1, now-1]:
        if 0 <= next_ < MAX_SIZE:
            if check[next_]==-1 or check[next_]=check[now]+1:
                check[next_]=check[now]+1
                queue.append(next_)

print(check[k])
print(cnt)