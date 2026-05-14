class MedianFinder:

    def __init__(self):
        self.list = SortedList()

    def addNum(self, num: int) -> None:
        self.list.add(num)

    def findMedian(self) -> float:
        n = len(self.list)
        mid = n // 2 
        if n % 2 == 0:
            return (self.list[mid] + self.list[mid-1]) / 2
        
        return self.list[mid]
