class MedianFinder:

    def __init__(self):
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        if not self.nums:
            return None

        n = len(self.nums)
        mid = n // 2

        if n % 2 != 0:
            return self.nums[mid]
        else:
            return (self.nums[mid - 1] + self.nums[mid]) / 2