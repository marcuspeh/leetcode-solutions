class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validLine = {"electronics", "grocery", "pharmacy", "restaurant"}
        
        arr = []
        for i in range(len(code)):
            currCode = code[i]
            currLine = businessLine[i]
            currActive = isActive[i]

            if self.validCode(currCode) and \
                    currLine in validLine and \
                    currActive:
                arr.append((currLine, currCode))
        
        arr.sort()
        result = []
        for _, code in arr:
            result.append(code)
        return result

    def validCode(self, code):
        if len(code) == 0:
            return False

        for char in code:
            if char == "_":
                continue
            if char.isalnum():
                continue
            return False
        return True