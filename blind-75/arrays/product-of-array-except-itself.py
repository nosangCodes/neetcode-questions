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
        
    print(prefixes)
    print(suffixes)
        
    return result

print(productExceptSelf([1,2,3,4]))