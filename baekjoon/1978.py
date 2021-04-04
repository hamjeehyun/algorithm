def is_prime(n):
    # 소수면 True
    if n==1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n=int(input())
arr=list(map(int, input().split()))

cnt=0

for i in range(n):
    result=is_prime(arr[i])
    if result == True:
        cnt+=1

print(cnt)