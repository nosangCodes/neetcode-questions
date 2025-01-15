def topKels(nums: list[int], k: int):
    # count = {}
    
    # for num in nums:
    #     count[num] = count.get(num, 0) + 1
    
    # arr = []
    # for num, cnt in count.items():
    #     arr.append([num, cnt])
    
    # arr.sort()
    
    # result = []
    
    # print(arr)
    # while len(result) < k:
    #     result.append(arr.pop()[1])
    
    # return result
    
    # with bucket sort
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums:
        count[n] = count.get(n, 0) + 1
        
    for num, cnt in count.items():
        freq[cnt].append(num)
    
    result = []
    
    for i in range(len(freq) - 1, 0, -1):
        print(i)
        for n in freq[i]:
            result.append(n)
        
        if len(result) == k:
            return result
    
    return result
    

result = topKels([2,2,3,1,1,1], 2)
result2 = topKels([1], 1)
print(result)
print(result2)
