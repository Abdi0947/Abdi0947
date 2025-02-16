# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.i = defaultdict(tuple)  # Stores check-in details
        self.o = defaultdict(list)   # Stores travel times

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, startStation = self.i[id]
        totalTime = t - startTime
        self.o[(startStation, stationName)].append(totalTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.o[(startStation, endStation)]
        return sum(times) / len(times) if times else 0.0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)