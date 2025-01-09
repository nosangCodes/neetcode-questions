# [1,8,6,2,5,4,8,3,7]
def containerWithMostWater(height: list[int]):
    left, right = 0, len(height) - 1
    maxWater = 0
    
    while left < right:
        currentMax = min(height[left], height[right]) * (right - left)
        maxWater = max(maxWater, currentMax)
        
        if height[left] > height[right]:
            right-=1
        else:
            left+=1
        
    return maxWater


print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))
print(containerWithMostWater([1,1]))
    