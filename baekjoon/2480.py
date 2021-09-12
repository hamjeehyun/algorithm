a, b, c = map(int, input().split())

result = 0

# 같은 눈  3개
if a == b == c:
    result = 10000 + a * 1000

# 같은 눈  3개
elif a == b:
    result = 1000 + a * 100
elif b == c:
    result = 1000 + b * 100
elif c == a:
    result = 1000 + c * 100

# 모두 다른 눈
else:
    result = max(a, b, c) * 100

print(result)