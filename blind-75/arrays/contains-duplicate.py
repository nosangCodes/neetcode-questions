def hasDuplicate(nums: list[int]):
    hashMap = {}
    
    for i, num in enumerate(nums):
        hashMap[num] = hashMap.get(num, 0) + 1
    
    for x in hashMap.keys():
        if hashMap[x] > 1:
            return True

    print(hashMap)
    return False
    
print(hasDuplicate([1, 2,2, 3]))