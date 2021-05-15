import sys
input = sys.stdin.readline

def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str, result)))
        return 
    
    for i in range(start, n):
        if visited[i]:
            continue

        visited[i] = True
        result.append(arr[i])

        go(index+1, i+1, n, m)

        result.pop()
        visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
visited=[False] * n

go(0, 0, n, m)