class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexes = defaultdict(list)
        
        for i, num in enumerate(nums):
            indexes[num].append(i)
        
        res = [0] * len(nums)
        
        def solve(num):
            arr = indexes[num]

            total = 0 
            for i in range(1,len(arr)):
                total += arr[i] - arr[0]

            res[arr[0]] = total

            for i in range(1, len(arr)):
                idx = arr[i]
                total += (arr[i] - arr[i-1]) * (i + 1)
                total -= (arr[i] - arr[i-1]) * (len(arr) - (i-2)-1)
                res[idx] = total
        
        for num in indexes.keys():
            solve(num)
        
        return res