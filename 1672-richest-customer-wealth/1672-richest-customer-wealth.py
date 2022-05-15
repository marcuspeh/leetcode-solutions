class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        
        for customer in accounts:
            maxi = max(maxi, sum(customer))
            
        return maxi