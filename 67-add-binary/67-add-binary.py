class Solution:
    def halfAdder(self, a, b, carry):
        if a == "0" and b == "0":
            # 0 + 0 + carry
            return carry, "0"
        elif a == "1" and b == "1":
            # 1 + 1 + carry
            return carry, "1"
        elif carry == "1":
            # 0/1 + 1/0 + 1
            return "0", carry
        else:
            # 0/1 + 1/0 + 0
            return "1", "0"
        
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = "0"
        
        aPointer = len(a) - 1
        bPointer = len(b) - 1
        
        while aPointer >= 0 and bPointer >= 0:
            temp, carry = self.halfAdder(a[aPointer], b[bPointer], carry)
            result.insert(0, temp)
            aPointer -= 1
            bPointer -= 1
            
        while aPointer >= 0:
            temp, carry = self.halfAdder(a[aPointer], "0", carry)
            result.insert(0, temp)
            aPointer -= 1
            
        while bPointer >= 0:
            temp, carry = self.halfAdder(b[bPointer], "0", carry)
            result.insert(0, temp)
            bPointer -= 1
            
        if carry == "1":
            result.insert(0, carry)
        
        return "".join(result)
            