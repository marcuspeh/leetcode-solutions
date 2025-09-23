class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        for i in range(max(len(version1), len(version2))):  
            part1 = 0
            if i < len(version1):
                part1 = int(version1[i])

            part2 = 0
            if i < len(version2):
                part2 = int(version2[i])
            
            if part1 > part2:
                return 1 
            if part1 < part2:
                return -1

        return 0
