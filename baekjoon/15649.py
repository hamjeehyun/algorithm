import sys
input = sys.stdin.readline

def go(index, n, m):
    # 종료조건: m개를 다 골랐다면 수열 출력
    if index == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(0, n):
        # 사용: T, 미사용: F
        if c[i]: 
            continue # 사용한 것이라면 넘기기

        c[i] = True # 사용
        arr.append(i+1) # arr 입력
        go(index+1, n, m)
        c[i] = False
        arr.pop()

    
n, m = map(int, input().split())
c = [False] * 10
arr =[]

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
go(0, n, m);