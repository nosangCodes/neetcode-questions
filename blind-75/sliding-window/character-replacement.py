def characterReplacement(s: str, k: int):
    count = {}
    maxF, left, result = 0, 0, 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        maxF = max(maxF, count[s[right]])
        
        while (right - left + 1) - maxF > k:
            count[s[left]]-=1
            left+=1
        
        result = max(right-left+1, result)
    
    return result

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))