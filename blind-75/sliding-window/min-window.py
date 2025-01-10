def minWindow(s: str, t: str):
    if not s or not t:
        return ""
    if len(t) > len(s):
        return ""
    
    countS, countT = {}, {}
    have = need = left = 0
    
    for ch in t:
        countT[ch] = countT.get(ch, 0) + 1
    
    need = len(countT.keys())
    result = []
    reslen = float('inf')
    
    for right in range(len(s)):
        countS[s[right]] = countS.get(s[right], 0) + 1
        
        if s[right] in countT and countT[s[right]] == countS[s[right]]:
            have+=1
            
        while have == need:
            if right - left + 1 < reslen:
                reslen = min(right - left + 1, reslen)
                result = [left, right]
            
            countS[s[left]]-=1
            if s[left] in countT and countS[s[left]] < countT[s[left]]:
                have-=1
            left+=1
    
    return "" if not result else s[result[0]: result[1] + 1]
            
            
    
result = minWindow("ADOBECODEBANC", "ABC")
result1 = minWindow("a", "a")
result2 = minWindow("a", "aa")
print(result)    
print(result1)    
print(result2)    
