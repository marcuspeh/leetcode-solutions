class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        alternate = []
        for string in strs:
            for i in range(len(string)):
                if len(alternate) == i:
                    alternate.append([])
                alternate[i].append(string[i])
        
        result = 0
        for arr in alternate:
            isSorted = True
            for i in range(1, len(arr)):
                if arr[i - 1] > arr[i]:
                    isSorted = False
                    break
            
            if not isSorted:
                result += 1
        
        return result