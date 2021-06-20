class Solution(object):
    def twoSum(nums, target):
        ans = {}
        for index, num in enumerate(nums): # enumerate: index 와 value를 같이 반환
            a = target - num

            if a in ans:
                return [ans[a], index]
            else: 
                ans[num] = index
        return []

print(Solution.twoSum([2,7,11,15], 9))
        