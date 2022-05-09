class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "1": [], 
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        def helper(curr, index):
            nonlocal result
            if len(digits) <= index:
                if curr:
                    result.append(curr)
                return
                
            number = digits[index]
            
            if number == 1:
                helper(curr, index + 1)
            else:
                for i in mapping[number]:
                    helper(curr + i, index + 1)
                    
        helper("", 0)
        return result