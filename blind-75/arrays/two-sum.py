# O(n**2)
def twoSum(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
                break
    
    return []

# print(twoSum([3,2,4], 5))

def twoSumOptimised(nums:list[int], target: int):
    n = len(nums)
    hashmap = {}
    
    for i in range(n):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    return []
        
print(twoSumOptimised([3,2,4], 5))