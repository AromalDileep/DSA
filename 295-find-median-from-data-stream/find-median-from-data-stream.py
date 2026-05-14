import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        
        # push into max heap
        heapq.heappush(self.small, -num)

        # move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # balance heaps
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -self.small[0]
        
        return (-self.small[0] + self.large[0]) / 2