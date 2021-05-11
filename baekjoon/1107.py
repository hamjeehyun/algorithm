import sys
input = sys.stdin.readline
MAX = 1000000

btn=[False] * 10
ch = int(input())
m = int(input())
a = list(map(int, input().split()))

for x in a:
    btn[x] = True

# 이동하려고 하는 채널까지 숫자를 눌러 이동 가능할 때, 
# 누르는 버튼의 개수를 반환
def possible(ch):
    if ch == 0:
        if btn[0]:
            return 0
        else:
            return 1
    len = 0
    while ch > 0:
        if btn[ch%10]:
            return 0
        len += 1
        ch //= 10
    return len

# 가장 처음에 보고 있는 채널은 100이기 때문에
# 초기값을 100에서 숫자 버튼을 누르지 않고 이동하는 횟수로 지정
answer = abs(ch - 50)

# 이동 가능한 모든 버튼을 검사
for i in range(100):
    len = possible(i)
    print(i, len)

    # 숫자를 눌러서 갈 수 있는 경우
    if len > 0:
        press = abs(i-ch) # +나 - 버튼을 몇 번 눌러야 하는지

        if answer > len + press:
            answer = len + press
print(answer)