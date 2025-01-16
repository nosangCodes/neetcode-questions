def productExceptSelf(nums: list[int]) -> list[int]:
    
    result = []
    
    prefixes = []
    prefixProduct = 1
    for num in nums:
        prefixes.append(prefixProduct)            
        prefixProduct*=num
        
    suffixes = [1] * len(nums)
    
    suffixProduct = 1
    for i in range(len(nums), 0, -1):
        suffixes[i - 1] = suffixProduct
        suffixProduct *= nums[i-1]
        

    for i in range(len(nums)):
        result.append(prefixes[i] * suffixes[i])
        
    return result

print(productExceptSelf([1,2,3,4]))


def bfSol(nums: list[int]):
    result = [0] * len(nums) 
    
    for i in range(len(nums)):
        currentProduct = 1
        for j in range(len(nums)):
            if i != j:
                currentProduct *= nums[j]
        result[i] = currentProduct
        
    return result


print(bfSol([1, 2, 3, 4]))
print(bfSol([-1,1,0,-3,3]))
print(productExceptSelf([-1,1,0,-3,3]))
    