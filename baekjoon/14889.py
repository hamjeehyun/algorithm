import sys
input = sys.stdin.readline

def go(index, first, second):
    # 종료
    if index == n:
        if len(first) != n // 2:
            return -1
        if len(second) != n // 2:
            return -1

        # 각 팀의 능력치 차이 구하기
        t1 = 0
        t2 = 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                t1 += arr[first[i]][first[j]]
                t2 += arr[second[i]][second[j]]
        
        diff = abs(t1 - t2)
        return diff

    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1

    answer = -1
    t1 = go(index + 1, first+[index], second)
    if answer == -1 or (t1 != -1 and answer > t1):
        answer = t1

    t2 = go(index + 1, first, second+[index])
    if answer == -1 or (t2 != -1 and answer > t2):
        answer = t2
    
    return answer

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))