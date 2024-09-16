class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeMinutes = list(map(self.convertToMinutes, timePoints))
        timeMinutes.sort()
        
        result = float("inf")
        for i in range(len(timeMinutes)):
            result = min(result, self.diff(timeMinutes[i - 1], timeMinutes[i]))
        return result
    
    def diff(self, time1, time2):
        return min(abs(time1 - time2), abs(1439 - time1 + time2 + 1), abs(1439 - time2 + time1 + 1))
        
    def convertToMinutes(self, time):
        hours, mins = time.split(":")
        return int(hours) * 60 + int(mins)