class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1List = list(map(lambda x: int(x), version1.split(".")))
        version2List = list(map(lambda x: int(x), version2.split(".")))
        
        pointer1 = 0
        pointer2 = 0
        
        for i in range(max(len(version1List), len(version2List))):
            first = version1List[i] if i < len(version1List) else 0
            second = version2List[i] if i < len(version2List) else 0
            if first < second:
                return -1
            elif first > second:
                return 1
        
        return 0