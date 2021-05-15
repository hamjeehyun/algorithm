import sys
input = sys.stdin.readline

def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n):
        arr.append(i+1)

        go(index+1, i+1, n, m)
        arr.pop()

n, m = map(int, input().split())
arr = []

go(0, 0, n, m)