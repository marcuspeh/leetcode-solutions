class Solution:
    def bestClosingTime(self, customers: str) -> int:
        openButNoCust = []
        for customer in customers:
            curr = openButNoCust[-1] if openButNoCust else 0
            curr += 1 if customer == "N" else 0 
            openButNoCust.append(curr)
        
        closeButCust = []
        for i in range(len(customers) - 1, -1, -1):
            customer = customers[i]
            curr = closeButCust[-1] if closeButCust else 0
            curr += 1 if customer == "Y" else 0
            closeButCust.append(curr)
        closeButCust.reverse()
            
        minPenalty = float('inf')
        time = 0        
        for i in range(len(customers)):
            curr = closeButCust[i]
            curr += openButNoCust[i - 1] if i - 1 >= 0 else 0
            if minPenalty <= curr:
                continue
            minPenalty = curr
            time = i
        
        if openButNoCust[-1] < minPenalty:
            return len(customers)
    
        return time