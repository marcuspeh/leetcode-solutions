class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteDegree = minutes * 6 # 6 degree per minute
        hourDegree = (hour * 60 + minutes) / 2 # 0.5 degree a minute
        diff = abs(minuteDegree - hourDegree)
        return min(diff, 360 - diff)