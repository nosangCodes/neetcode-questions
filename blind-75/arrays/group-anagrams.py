def groupAnagrams(strs: list[str]) -> list[list[str]]:
    sortedStrs = []
    hashMap = {}    
    for str in strs:
        sortedStrs.append("".join(sorted(str)))
    
    for i, str in enumerate(sortedStrs):
        if str in hashMap:
            hashMap[str].append(strs[i])
        else:
            hashMap[str] = [strs[i]]
            
    return list(hashMap.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

