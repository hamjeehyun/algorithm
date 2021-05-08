def is_prime(n):
    # 소수면 True
    if n<2:
        return False
    i=2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

n=int(input())
arr=list(map(int, input().split()))

cnt=0
    
for a in arr:
    if is_prime(a): cnt += 1

print(cnt)