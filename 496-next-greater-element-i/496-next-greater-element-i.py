class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        result = []
        
        for n in nums2:
            while stack and stack[-1] < n:
                temp = stack.pop()
                mapping[temp] = n
            stack.append(n)
            
        for n in nums1:
            if n in mapping:
                result.append(mapping[n])
            else:
                result.append(-1)
                
        return result