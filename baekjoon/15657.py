import sys
input = sys.stdin.readline

def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return 

    for i in range(start, n):
        result.append(arr[i])

        go(index+1, i, n, m)

        result.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

go(0, 0, n, m)