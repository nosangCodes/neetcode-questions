# [-1,0,1,2,-1,-4]
def threeSum(nums: list[int]):
    nums.sort()
    result = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left+=1
                
                while nums[left] == nums[left + 1] and left < right:
                    left+=1
                
            elif currentSum > 0:
                right-=1
            else:
                left+=1
    
    return result


print(threeSum([-1,0,1,2,-1,-4]))
