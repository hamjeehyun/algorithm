n, s = map(int, input().split())
nums=list(map(int, input().split()))

nums_sum=[0] * (n+1)
for i in range(1, n+1):
    nums_sum[i]=nums_sum[i-1]+nums[i-1]

answer=100001
start=0
end=1

while start != n:
    if nums_sum[end]-nums_sum[start] >= s:
        if end-start < answer:
            answer=end-start
        start+=1

    else:
        if end != n:
            end+=1
        else:
            start+=1

if answer != 100001:
    print(answer)
else:
    print(0)