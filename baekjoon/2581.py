def is_prime_number(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

a=int(input())
b=int(input())
arr=[]

for i in range(a, b+1):
    result=is_prime_number(i)
    if result:
        arr.append(i)

if len(arr)>0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)