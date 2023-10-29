class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        
        maxTries = minutesToTest // minutesToDie + 1
         
        """
        Suppose maxTries = 3, buckets / round1 / round2 / round3 == 1
        
        Can pictures as a tree with maxTries level and buckets number of leave nodes
        """
        logBucket = math.log(buckets)
        logTries = math.log(maxTries)
        return int(logBucket // logTries + (1 if abs(logBucket % logTries) > 0.001 else 0))