import sys
input=sys.stdin.readline

def check(arr):
    n=len(arr)
    answer=1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt=1
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt=1
            if cnt > answer:
                answer = cnt

    return answer

n=int(input())
arr=[list(input()) for _ in range(n)]
answer=0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp=check(arr)

            if temp > answer:
                answer = temp

            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 바꾸기
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp=check(arr)

            if temp > answer:
                answer = temp

            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(answer)