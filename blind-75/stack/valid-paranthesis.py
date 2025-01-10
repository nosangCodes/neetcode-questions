def validParanthesis(s: str):
    
    brackets = {
        '(': ')',
        '[': ']',
        "{": "}"
    }
    
    stack = []
    
    for ch in s:
        if ch in brackets:
            stack.append(brackets[ch])
        elif len(stack) > 0 and ch == stack[-1]:
            stack.pop()
        else:
            return False
    return True

print(validParanthesis("()[]){}"))
print(validParanthesis("(]"))
print(validParanthesis("()[]{}"))
        