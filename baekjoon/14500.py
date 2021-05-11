import sys
input = sys.stdin.readline

m, n = map(int, input().split())

arr = []
for _ in range(m):
    a = list(map(int, input().split()))
    arr.append(a)

answer = 0
for i in range(m):
    for j in range(n):
        # 1
        if j+3 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
            if tmp > answer:
                answer = tmp

        # 2
        if i+3 < m:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
            if tmp > answer:
                answer = tmp
        
        # 3
        if i+1 < m and j+1 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
            if tmp > answer:
                answer = tmp
        
        # 4
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
            if tmp > answer:
                answer = tmp
        
        # 5
        if i+2 < m and j-1 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
            if tmp > answer:
                answer = tmp

        # 6
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j]
            if tmp > answer:
                answer = tmp

        # 7
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
            if tmp > answer:
                answer = tmp

        # 8
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
            if tmp > answer:
                answer = tmp
        
        # 9
        if i+1 < m and j-2 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j-2]
            if tmp > answer:
                answer = tmp

        # 10
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i][j+1]
            if tmp > answer:
                answer = tmp

        # 11
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
            if tmp > answer:
                answer = tmp

        # 12
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
            if tmp > answer:
                answer = tmp

        # 13
        if i+2 < m and j-1 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j-1]
            if tmp > answer:
                answer = tmp

        # 14
        if i-1 >= 0 and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i-1][j+2]
            if tmp > answer:
                answer = tmp

        # 15
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
            if tmp > answer:
                answer = tmp

        # 16
        if i-1 >= 0 and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+1]
            if tmp > answer:
                answer = tmp
        
        # 17
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
            if tmp > answer:
                answer = tmp

        # 18
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j]
            if tmp > answer:
                answer = tmp

        # 19
        if i+2 < m and j-1 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j]
            if tmp > answer:
                answer = tmp
print(answer)