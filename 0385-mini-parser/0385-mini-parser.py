# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    @cache
    def getNextToken(self, s, startingIdx):
        if startingIdx >= len(s):
            return "", startingIdx
        
        if s[startingIdx] in ("]", "[", ","):
            return s[startingIdx], startingIdx + 1
    
        number = ""
        while startingIdx < len(s) and s[startingIdx] not in ("]", "[", ","):
            number += s[startingIdx]
            startingIdx += 1
        
        return int(number), startingIdx
    
    def deserialize(self, s: str) -> NestedInteger:
        def helper(idx):
            nextToken, idx = self.getNextToken(s, idx)
            
            if nextToken == "":
                return NestedInteger(), idx
            
            if type(nextToken) == int:
                return NestedInteger(nextToken), idx
            
            if nextToken != "[":
                raise Exception(f"Unexpected token {nextToken}") 
            
            result = NestedInteger()
            newToken, newIdx = self.getNextToken(s, idx)
            while newToken != "]":
                if newToken == ",":
                    idx = newIdx
                    newToken, newIdx = self.getNextToken(s, idx)
                    continue
                    
                if newToken == "[":
                    newArr, idx = helper(idx)
                    result.add(newArr)
                    newToken, newIdx = self.getNextToken(s, idx)
                    continue
                
                idx = newIdx
                result.add(NestedInteger(newToken))
                newToken, newIdx = self.getNextToken(s, idx)
            return result, idx + 1
            
        
        return helper(0)[0]
        
        