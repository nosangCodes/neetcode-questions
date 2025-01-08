class EncodeDecodeStr:
    
    def encode(self, strs: list[str]):
        result = ""
        for str in strs:
            result += f"{len(str)}#{str}"
        return result
    
    def decode(self, eStr):
        i = 0
        result = []
        
        while i < len(eStr):
            j = i
            while eStr[j] != "#":
                j+=1
            wordLen = int(eStr[i:j])
            i=j+1
            j = i + wordLen
            
            result.append(eStr[i:j])            
            i = j
        return result
            
    
            

encodeDecode =  EncodeDecodeStr()

encodedStr = encodeDecode.encode(["neet","code","love","you"])
decodedStr = encodeDecode.decode(encodedStr)

print(encodedStr)
print(decodedStr)