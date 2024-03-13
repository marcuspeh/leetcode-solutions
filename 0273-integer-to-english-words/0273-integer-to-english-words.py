class Solution:
    tenPlace = [
        "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    below20 = [
        "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    ]
        
    def calculateBillion(self, num, result):
        if num < 1000000000:
            return num
        idx = num // 1000000000 - 1
        result.append(Solution.below20[idx])
        result.append("Billion")
        return num % 1000000000

    def calculateMillion(self, num, result):
        if num < 1000000:
            return num
        
        temp = self.calculateHundred(num // 1000000, result)
        self.calculateTen(temp, result)
        result.append("Million")
        return num % 1000000
    
    def calculateThousand(self, num, result):
        if num < 1000:
            return num
        
        temp = self.calculateHundred(num // 1000, result)
        self.calculateTen(temp, result)
        result.append("Thousand")
        return num % 1000
    
    def calculateHundred(self, num, result):
        if num < 100:
            return num
    
        idx = num // 100 - 1
        result.append(Solution.below20[idx])
        result.append("Hundred")
        return num % 100
    
    def calculateTen(self, num, result):
        if num <= 0:
            return 
        
        if num < 20:
            result.append(Solution.below20[num - 1])
            return 0
        
        tenthPlaceIdx = num // 10 - 1
        result.append(Solution.tenPlace[tenthPlaceIdx])
        if num % 10 > 0:
            result.append(Solution.below20[num % 10 - 1])
        return 0
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
  
        result = []
        num = self.calculateBillion(num, result)
        num = self.calculateMillion(num, result)
        num = self.calculateThousand(num, result)
        num = self.calculateHundred(num, result)
        self.calculateTen(num, result)
        return " ".join(result)
        