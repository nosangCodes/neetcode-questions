def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hashS = {}
    
    for ch in s:
        hashS[ch] = hashS.get(ch, 0) + 1
    
    for ch in t:
        if ch in hashS and hashS[ch] > 0:
            hashS[ch]-=1
        else:
            return False
    
    return all(value == 0 for value in hashS.values())
    
print(isAnagram("rat", "car"))