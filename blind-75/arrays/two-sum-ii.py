def twoSumII(numbers:list, target: int):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        currSum = numbers[left] + numbers[right]
        print(currSum)
        if currSum == target:
            return [left + 1, right + 1]
        elif target < currSum:
            right-=1
        else:
            left+=1
    return []


print(twoSumII([2,7,11,15], 9))
print(twoSumII([2,3,4], 6))