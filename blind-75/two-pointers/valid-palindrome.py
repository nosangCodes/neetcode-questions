def validPalindrome(s: str):
    formattedStr = "".join(filter(str.isalnum, s)).lower()
    
    left = 0
    right = len(formattedStr) - 1
    
    while left < right:
        if formattedStr[left] != formattedStr[right]:
            return False
        left+=1
        right-=1
    
    return True
    
    

print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))
print(validPalindrome(""))