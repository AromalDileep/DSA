class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(num % value for num in nums)
        print(cnt)
        # Find the smallest non-negative integer not representable
        i = 0
        while True:
            if cnt[i % value] == 0:
                return i
            cnt[i % value] -= 1
            i += 1
