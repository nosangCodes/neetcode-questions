def longestConsecSeq(nums: list[int]) -> int:
    longestStreak = 0
    numSet = set(nums)
    print(numSet)
    
    for i in range(len(nums)):
        if nums[i] - 1 not in numSet:
            currentStreak = 1
            currentNum = nums[i]
            
            while currentNum + 1 in numSet:
                currentNum += 1
                currentStreak += 1
                
            longestStreak = max(currentStreak, longestStreak)
    
    return longestStreak


# print(longestConsecSeq([0,3,7,2,5,8,4,6,0,1]))
# print(longestConsecSeq([100,4,200,1,3,2]))

