nums = [1,1,2]
cnt=1
next=1

for i in range(len(nums)):
    if next < len(nums) and nums[i] != nums[next]:
        cnt += 1
        next += 1
    else:
        next += 1

print(cnt) 
