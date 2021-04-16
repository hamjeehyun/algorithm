from collections import deque
import sys
input=sys.stdin.readline
MAX_SIZE=1001

s=int(input())
check=dict()
check[(1, 0)]=0

queue=deque()
queue.append((1, 0))

while queue:
    now, clipboard = queue.popleft()

    if now==s:
        print(check[(now, clipboard)])
        break

    cal=[now, now+clipboard, now-1]
    for next_ in cal:
        # print('next_', next_)
        if 0 <= clipboard < MAX_SIZE and 0 < next_ < MAX_SIZE and (next_, now) not in check.keys():
            if cal.index(next_)==0:
                queue.append((next_, next_))
                check[(next_, next_)] = check[(now, clipboard)]+1
            else:
                queue.append((next_, clipboard))
                check[(next_, clipboard)] = check[(now, clipboard)]+1