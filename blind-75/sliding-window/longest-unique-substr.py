def lengthOfLongestSubstring(s: str):
    strSet = set()
    left = 0
    result = 0
    
    for right in range(len(s)):
        while s[right] in strSet:
            strSet.remove(s[left])
            left+=1
        
        strSet.add(s[right])
        result = max(result, right - left + 1)
    
    return result

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))