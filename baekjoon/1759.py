import sys
input = sys.stdin.readline

def check(password):
    ja = 0 # 자음 갯수
    mo = 0 # 모음 갯수

    for x in password:
        if x in 'aeiou':
            # 해당 password에 모음 갯수 세기
            mo += 1 
        else:
            # 해당 password에 자음 갯수 세기
            ja += 1

    # 최소 한 개의 모음과 최소 두 개의 자음이 포함 되어 있다면 True
    return ja >= 2 and mo >= 1

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
            return
    
    if i == len(alpha):
        return

    # i 번째 알파벳을 사용하는 경우
    go(n, alpha, password+alpha[i], i+1)

    # i 번째 알파벳을 사용하지 않는 경우
    go(n, alpha, password, i+1)


# L: 암호의 길이 C: 주어지는 알파벳 수
L, C = map(int, input().split())
c_arr = input().split()

# 정렬
c_arr.sort()

go(L, c_arr, "", 0)