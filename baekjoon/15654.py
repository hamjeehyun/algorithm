import sys
input = sys.stdin.readline

def go(index, n, m):
    if index == m:
        print(' '.join(map(str, result)))

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        result.append(arr[i])

        go(index+1, n, m)

        visited[i]=False
        result.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * 10
result = []

go(0, n, m)