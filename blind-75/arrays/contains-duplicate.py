def hasDuplicate(nums: list[int]):
    hashMap = {}
    
    for i, num in enumerate(nums):
        hashMap[num] = hashMap.get(num, 0) + 1
    
    for x in hashMap.keys():
        if hashMap[x] > 1:
            return True

    print(hashMap)
    return False
    
# print(hasDuplicate([1, 2,2, 3]))

def containsDuplicate(nums: list[int]):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(containsDuplicate([1, 2,2, 3]))
print(containsDuplicate([1, 2, 3, 4]))