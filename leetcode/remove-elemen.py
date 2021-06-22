nums=[0,1,2,2,3,0,4,2]
val=2

for num in range(len(nums)):
    if nums[0] != val:
        nums.append(nums[0])
        del nums[0]
    else:
        del nums[0]
    
print(nums)

