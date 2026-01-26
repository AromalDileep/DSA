class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diffs = {}
        minimum = float("inf")

        for i in range(1, len(arr)):
            diffs[(arr[i-1], arr[i])] = arr[i] - arr[i-1] 
            minimum = min(minimum, arr[i]-arr[i-1])
        
        result = []

        for key, val in diffs.items():
            if val == minimum:
                result.append(list(key))

        return result
