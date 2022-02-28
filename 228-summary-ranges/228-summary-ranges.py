class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = None
        end = None
        
        for i in nums:
            if start == end and end == None:
                start = i
                end = i
            elif i == end + 1:
                end = i
            else:
                if start == end:
                    result.append(f'{start}')
                else:
                    result.append(f'{start}->{end}')
                
                start = i
                end = i
        
        if start == end:
            result.append(f'{start}')
        else:
            result.append(f'{start}->{end}')
            
        return result