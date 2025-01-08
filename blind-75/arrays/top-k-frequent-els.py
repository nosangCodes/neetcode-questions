def topKels(nums: list[int], k: int):
    hashMap = {}
    
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
    sortedFreq = sorted(hashMap.items(), key=lambda x:x[1], reverse=True)
    
    print([item[0] for item in sortedFreq[:k]])
    

topKels([1,1,1,2,2,3], 2)