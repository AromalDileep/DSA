class MedianFinder:

    def __init__(self):
        #  (Max Heap)
        self.small = []  
        # (Min Heap)
        self.large = []  

    def addNum(self, num: int) -> None:
        # 1. Push to small (max heap)
        heapq.heappush_max(self.small, num)

        # 2. Balance: move largest of small to large (min heap)
        heapq.heappush(self.large, heapq.heappop_max(self.small))

        # 3. Maintain size: small can be equal or 1 greater than large
        if len(self.large) > len(self.small):
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(self.small[0])
        return (self.small[0] + self.large[0]) / 2
